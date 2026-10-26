"""Exercise the public checker against disposable Git repositories, never live CI."""

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / 'scripts/check-docs'


class DocumentationChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='daedalus-doc-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        subprocess.run(['git', 'init', '--quiet', str(self.root)], check=True)
        rows = []
        for version in ('v1.0', 'v1.1'):
            name = f'docs/standards/git-github-workflow/{version}.md'
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)
            digest = hashlib.sha256(target.read_bytes()).hexdigest()
            rows.append(f'| [{version}](git-github-workflow/{version}.md) | `{digest}` |')
        self.put('docs/standards/README.md', '# Catalog\n\n| File | SHA-256 |\n| --- | --- |\n' +
                 '\n'.join(rows) + '\n')
        self.put('docs/engineering.md', '# Engineering\n\n## Agent Engineering Workflow\n\n'
                 '[Unique body](agent-workflow.md)\n')
        self.put('docs/agent-workflow.md', '# Agent Engineering Workflow\n\nProposed.\n')

    def put(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')

    def check(self, *args):
        return subprocess.run([sys.executable, str(CHECK), '--root', str(self.root), *args],
                              text=True, capture_output=True, cwd=self.temp.name)

    def assert_good(self):
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def assert_bad(self, message):
        result = self.check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(message, '\n'.join(json.loads(result.stdout)['errors']))

    def test_valid_untracked_documents_and_heading_collisions(self):
        self.put('new.md', '# 标题 `Example`\n\n## Repeat\n## Repeat\n## Repeat-1\n\n'
                 '[Unicode](#标题-example) [Repeat](#repeat-1) [Collision](#repeat-1-1)\n')
        self.assertEqual(self.assert_good()['counts']['markdown'], 6)

    def test_untracked_missing_target_fails(self):
        self.put('new.md', '# New\n\n[Missing](absent.md)\n')
        self.assert_bad('missing or uninspected target')

    def test_missing_anchor_fails(self):
        self.put('new.md', '# New\n\n[Missing](docs/engineering.md#absent)\n')
        self.assert_bad('missing Markdown anchor')

    def test_reference_links_and_spaces(self):
        self.put('space name.md', '# Target\n')
        self.put('new.md', '# New\n\n[space](<space name.md#target>)\n'
                 '[label][target]\n[target][]\n[target]\n\n'
                 '[target]: <space name.md#target> "title"\n')
        self.assert_good()

    def test_invalid_reference_definition_fails(self):
        self.put('new.md', '# New\n\n[use][label]\n\n[label]: missing.md\n')
        self.assert_bad('missing or uninspected target')

    def test_plain_bracketed_citations_are_not_links(self):
        self.put('new.md', '# New\n\nReference [R02][R03].\n\n**[R02] Source**\n')
        self.assert_good()

    def test_parentheses_and_external_links(self):
        self.put('a(b).md', '# Target\n')
        self.put('new.md', '# New\n\n[local](a(b).md#target)\n'
                 '[external](https://example.invalid/missing)\n')
        self.assert_good()

    def test_code_examples_do_not_create_navigation(self):
        self.put('new.md', '# New\n\n`[inline](absent.md)`\n\n'
                 '````text\n[example](absent.md)\n```\n````\n\n'
                 '| A | B |\n| --- | --- |\n| `a|b` | c \\| d |\n')
        self.assert_good()

    def test_structure_and_whitespace_failures(self):
        for text, expected in (
            ('# Title\n\n```text\nnot closed\n', 'unclosed code fence'),
            ('# Title  \n', 'trailing whitespace'),
            ('# Title', 'final newline'),
            ('# Title\r\n', 'use LF'),
            ('# Title\n\n| A | B |\n| --- | --- |\n| only one |\n', 'table columns'),
        ):
            with self.subTest(expected=expected):
                self.put('new.md', text)
                self.assert_bad(expected)

    def test_invalid_utf8_fails(self):
        (self.root / 'new.md').write_bytes(b'# Title\n\xff\n')
        self.assert_bad('unreadable UTF-8')

    def test_tracked_deletion_fails(self):
        self.put('tracked.md', '# Tracked\n')
        subprocess.run(['git', '-C', str(self.root), 'add', 'tracked.md'], check=True)
        (self.root / 'tracked.md').unlink()
        self.assert_bad('unreadable UTF-8')

    def test_ignored_markdown_not_in_scope(self):
        self.put('.gitignore', 'ignored.md\n')
        self.put('ignored.md', '[broken](missing.md)\n')
        self.assert_good()

    def test_external_symlink_is_rejected(self):
        (self.root / 'outside.md').symlink_to(ROOT / 'README.md')
        self.assert_bad('document escapes repository')

    def test_frozen_change_rejected_even_with_updated_catalog(self):
        name = 'docs/standards/git-github-workflow/v1.1.md'
        path = self.root / name
        old = hashlib.sha256(path.read_bytes()).hexdigest()
        path.write_bytes(path.read_bytes() + b'\n')
        new = hashlib.sha256(path.read_bytes()).hexdigest()
        catalog = self.root / 'docs/standards/README.md'
        catalog.write_text(catalog.read_text().replace(old, new))
        self.assert_bad('Frozen digest mismatch')

    def test_missing_frozen_fails(self):
        (self.root / 'docs/standards/git-github-workflow/v1.0.md').unlink()
        self.assert_bad('Frozen digest mismatch or missing file')

    def test_candidate_digest_is_checked(self):
        catalog = self.root / 'docs/standards/README.md'
        catalog.write_text(catalog.read_text() +
                           '| [candidate](../agent-workflow.md) | `' + '0' * 64 + '` |\n')
        self.assert_bad('catalog full-file digest mismatch')

    def test_legacy_navigation_must_survive_migration(self):
        self.put('docs/engineering.md', '# Engineering\n')
        self.assert_bad('missing legacy Agent workflow anchor')

    def test_legacy_heading_alone_is_insufficient(self):
        self.put('docs/engineering.md', '# Engineering\n\n## Agent Engineering Workflow\n')
        self.assert_bad('must link to the unique body')

    def test_non_repository_fails_with_distinct_exit_status(self):
        shutil.rmtree(self.root / '.git')
        result = self.check()
        self.assertEqual(result.returncode, 2)
        self.assertIn('Cannot inspect repository', result.stderr)


if __name__ == '__main__':
    unittest.main()
