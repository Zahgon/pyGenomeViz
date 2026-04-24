#!/usr/bin/env python
from __future__ import annotations

import argparse
import logging
import os
from collections import defaultdict
from pathlib import Path
from typing import Sequence

from pygenomeviz import GenomeViz
from pygenomeviz.align import AlignCoord, ProgressiveMauve
from pygenomeviz.logger import init_logger
from pygenomeviz.scripts import (
    ALIGN_COORDS_FILENAME,
    LOG_FILENAME,
    CustomHelpFormatter,
    exit_handler,
    log_basic_env_info,
    logging_timeit,
    setup_argparser,
    validate_args,
)
from pygenomeviz.typing import PlotStyle, TrackAlignType
from pygenomeviz.utils import ColorCycler

CLI_NAME = "pgv-pmauve"


@exit_handler
def main():
    """Main function called from CLI"""
    pass


@logging_timeit
def run(
    # General options
    seqs: Sequence[str | Path],
    outdir: str | Path,
    formats: list[str],
    reuse: bool,
    quiet: bool,
    debug: bool,
    # Figure appearence options
    fig_width: float,
    fig_track_height: float,
    track_align_type: TrackAlignType,
    feature_track_ratio: float,
    show_scale_bar: bool,
    show_scale_xticks: bool,
    curve: bool,
    dpi: int,
    track_labelsize: int,
    scale_labelsize: int,
    normal_link_color: str,
    inverted_link_color: str,
    refid: int,
    block_plotstyle: PlotStyle,
    block_cmap: str,
):
    """Run genome visualization workflow"""
    pass


def get_args() -> argparse.Namespace:
    """Get arguments

    Returns
    -------
    args : argparse.Namespace
        Argument parameters
    """
    pass


if __name__ == "__main__":
    main()
