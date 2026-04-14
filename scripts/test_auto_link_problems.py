import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
import re


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "auto_link_problems.py"


class AutoLinkProblemsTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp(prefix="autolink-test-"))
        problems_dir = self.temp_dir / "content" / "problems"
        problems_dir.mkdir(parents=True, exist_ok=True)

        (problems_dir / "a-1-1.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Circuit Value Problem"
                acronym: 'CVP'
                ---

                ## Remarks

                Canonical base problem.
                """
            ),
            encoding="utf-8",
        )

        (problems_dir / "a-1-5.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "NAND Circuit Value Problem"
                acronym: "NANDCVP"
                ---

                ## Remarks

                NORCVP variant definition.
                """
            ),
            encoding="utf-8",
        )

        (problems_dir / "a-2-1.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Sample"
                acronym: "SAMPLE"
                references: [1]
                ---

                ## Remarks

                Reduction is from CVP.
                Already linked [CVP]({{< relref "./a-1-1.md" >}}).
                Also from NORCVP.
                """
            ),
            encoding="utf-8",
        )

        (problems_dir / "a-2-2.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Reciprocity Source"
                acronym: "SRC"
                related_problems:
                  - id: a-2-3
                    relation: reduces-from
                ---

                ## Remarks

                Source node.
                """
            ),
            encoding="utf-8",
        )

        (problems_dir / "a-2-3.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Reciprocity Target"
                acronym: "TGT"
                ---

                ## Remarks

                Target node.
                """
            ),
            encoding="utf-8",
        )

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def run_script(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT_PATH), "--root", str(self.temp_dir), *args],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )

    def test_check_mode_exits_non_zero_when_changes_needed(self):
        result = self.run_script("--check")
        self.assertNotEqual(result.returncode, 0)

    def test_rewrites_body_and_related_problems(self):
        first = self.run_script()
        self.assertEqual(first.returncode, 0, first.stderr)

        updated = (self.temp_dir / "content" / "problems" / "a-2-1.md").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            'Reduction is from [CVP]({{< relref "./a-1-1.md" >}}).',
            updated,
        )
        self.assertIn(
            'Already linked [CVP]({{< relref "./a-1-1.md" >}}).',
            updated,
        )
        self.assertIn(
            'Also from [NORCVP]({{< relref "./a-1-5.md" >}}).',
            updated,
        )
        self.assertIn("related_problems:", updated)
        self.assertIn("- id: a-1-1", updated)
        self.assertIn("- id: a-1-5", updated)
        self.assertIn("relation: see-also", updated)

        second = self.run_script("--check")
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)

    def test_preserves_frontmatter_style_and_appends_related_at_end(self):
        original = (self.temp_dir / "content" / "problems" / "a-2-1.md").read_text(encoding="utf-8")
        original_frontmatter = re.match(
            r"^\ufeff?---\r?\n(?P<front>.*?)(?:\r?\n)---\r?\n",
            original,
            re.DOTALL,
        ).group("front")
        self.assertIn('title: "Sample"', original_frontmatter)
        self.assertIn('acronym: "SAMPLE"', original_frontmatter)
        self.assertIn("references: [1]", original_frontmatter)

        first = self.run_script()
        self.assertEqual(first.returncode, 0, first.stderr)

        updated = (self.temp_dir / "content" / "problems" / "a-2-1.md").read_text(encoding="utf-8")
        updated_frontmatter = re.match(
            r"^\ufeff?---\r?\n(?P<front>.*?)(?:\r?\n)---\r?\n",
            updated,
            re.DOTALL,
        ).group("front")

        self.assertIn('title: "Sample"', updated_frontmatter)
        self.assertIn('acronym: "SAMPLE"', updated_frontmatter)
        self.assertIn("references: [1]", updated_frontmatter)
        self.assertTrue(updated_frontmatter.rstrip().endswith("relation: see-also"))

    def test_adds_reciprocal_reduction_relation(self):
        first = self.run_script()
        self.assertEqual(first.returncode, 0, first.stderr)

        target_updated = (self.temp_dir / "content" / "problems" / "a-2-3.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("- id: a-2-2", target_updated)
        self.assertIn("relation: reduces-to", target_updated)


if __name__ == "__main__":
    unittest.main()
