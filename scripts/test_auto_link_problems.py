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
                    relation: see-also
                  - id: a-2-3
                    relation: reduces-from
                  - id: a-2-4
                    relation: see-also
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

        (problems_dir / "a-2-4.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Unrelated Target"
                acronym: "UTGT"
                ---

                ## Remarks

                Target with only see-also.
                """
            ),
            encoding="utf-8",
        )

        (problems_dir / "a-8-7.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Sample SC Problem"
                acronym: "SC"
                ---

                ## Remarks

                Defines SC acronym target.
                """
            ),
            encoding="utf-8",
        )

        (problems_dir / "a-8-26.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Math Mode Sample"
                acronym: "MMS"
                ---

                ## Remarks

                Inside math: $\\mathsf{SC}^k$ should stay unchanged.
                Outside math: SC should become link.
                """
            ),
            encoding="utf-8",
        )

        (problems_dir / "a-9-9.md").write_text(
            textwrap.dedent(
                """\
                ---
                title: "Reference Link Sample"
                acronym: "RLS"
                references: [1, 2]
                book_id: "A.9.9"
                ---

                ## Remarks

                Bounded [1] and [2, Theorem 2.3] are standard.
                Split citations [1][2] should both link.
                Range [1,2] should remain unchanged for now.
                Book citation [3] should link.
                Out of range [4] should not.
                Inside code `[1]` stays.
                Inside math $[1]$ stays.
                Already linked [1](#ref-1) stays.
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

    def test_reduction_relations_override_see_also(self):
        first = self.run_script()
        self.assertEqual(first.returncode, 0, first.stderr)

        source_updated = (self.temp_dir / "content" / "problems" / "a-2-2.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("- id: a-2-3", source_updated)
        self.assertIn("relation: reduces-from", source_updated)
        self.assertNotIn("- id: a-2-3\n    relation: see-also", source_updated)
        self.assertIn("- id: a-2-4\n    relation: see-also", source_updated)

    def test_does_not_link_acronyms_inside_latex_math(self):
        first = self.run_script()
        self.assertEqual(first.returncode, 0, first.stderr)

        updated = (self.temp_dir / "content" / "problems" / "a-8-26.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Inside math: $\\mathsf{SC}^k$ should stay unchanged.", updated)
        self.assertIn('Outside math: [SC]({{< relref "./a-8-7.md" >}}) should become link.', updated)

    def test_links_in_page_reference_citations(self):
        first = self.run_script()
        self.assertEqual(first.returncode, 0, first.stderr)

        updated = (self.temp_dir / "content" / "problems" / "a-9-9.md").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            'Bounded <a href="#ref-1" class="reference-citation">[1]</a> and <a href="#ref-2" class="reference-citation">[2, Theorem 2.3]</a> are standard.',
            updated,
        )
        self.assertIn(
            'Split citations <a href="#ref-1" class="reference-citation">[1]</a><a href="#ref-2" class="reference-citation">[2]</a> should both link.',
            updated,
        )
        self.assertIn("Range [1,2] should remain unchanged for now.", updated)
        self.assertIn(
            'Book citation <a href="#ref-3" class="reference-citation">[3]</a> should link.',
            updated,
        )
        self.assertIn("Out of range [4] should not.", updated)
        self.assertIn("Inside code `[1]` stays.", updated)
        self.assertIn("Inside math $[1]$ stays.", updated)
        self.assertIn("Already linked [1](#ref-1) stays.", updated)


if __name__ == "__main__":
    unittest.main()
