from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

import pygenomeviz


def _concat_target_files_contents(files: list[Path], target_ext: str) -> str:
    """Concatenate target extension files contents"""
    contents = "\n"
    target_files = [file for file in files if file.suffix == target_ext]
    for target_file in target_files:
        with open(target_file, encoding="utf-8") as f:
            contents += f.read() + "\n"
    return contents


_viewer_dir = Path(__file__).parent
_assets_dir = _viewer_dir / "assets"
_assets_files = [
    "lib/spectrum.min.css",
    "lib/tabulator.min.css",
    "lib/micromodal.css",
    "lib/jquery.min.js",
    "lib/spectrum.min.js",
    "lib/panzoom.min.js",
    "lib/tabulator.min.js",
    "lib/micromodal.min.js",
    "lib/popper.min.js",
    "lib/tippy-bundle.umd.min.js",
    "pgv-viewer.js",
]
_assets_files = [_assets_dir / f for f in _assets_files]

TEMPLATE_HTML_FILE = _viewer_dir / "pgv-viewer-template.html"
CSS_CONTENTS = _concat_target_files_contents(_assets_files, ".css")
JS_CONTENTS = _concat_target_files_contents(_assets_files, ".js")


def setup_viewer_html(
    svg_figure: str,
    gid2feature_dict: dict[str, dict[str, Any]],
    gid2link_dict: dict[str, dict[str, Any]],
) -> str:
    """Setup viewer html (Embed SVG figure, CSS & JS assets)

    Parameters
    ----------
    svg_figure : str
        SVG figure strings
    gid2feature_dict : dict[str, dict[str, Any]]
        GID(Group ID) & feature dict
    gid2link_dict : dict[str, dict[str, Any]]
        GID(Group ID) & link dict

    Returns
    -------
    viewer_html : str
        Viewer html strings
    """
    pass
