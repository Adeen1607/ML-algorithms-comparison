"""Regression tests for stable figure extraction without external datasets."""
import ast
import base64
import hashlib
import json
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_research_site.py"


def load_extractor():
    # Load just the pure extractor, avoiding optional rendering dependencies.
    tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
    function = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "extract_figs")
    namespace = {"json": json, "base64": base64, "hashlib": hashlib, "Path": Path, "sorted": sorted}
    exec(compile(ast.Module(body=[function], type_ignores=[]), str(SCRIPT), "exec"), namespace)
    return namespace["extract_figs"]


class FigureExtractionTests(unittest.TestCase):
    def test_same_named_notebooks_do_not_overwrite_figures(self):
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp) / "repo"
            site = repo / "research"
            for folder, image in (("first", b"first-image"), ("second", b"second-image")):
                notebook = repo / folder / "analysis.ipynb"
                notebook.parent.mkdir(parents=True)
                notebook.write_text(json.dumps({"cells": [{"cell_type": "code", "metadata": {}, "outputs": [{"data": {"image/png": base64.b64encode(image).decode()}}]}]}))
            figures = load_extractor()(repo, site)
            self.assertEqual(len(figures), 2)
            self.assertEqual(len({path.name for path, _ in figures}), 2)
            self.assertEqual({path.read_bytes() for path, _ in figures}, {b"first-image", b"second-image"})
            self.assertEqual([path.name for path, _ in load_extractor()(repo, site)], [path.name for path, _ in figures])


if __name__ == "__main__":
    unittest.main()
