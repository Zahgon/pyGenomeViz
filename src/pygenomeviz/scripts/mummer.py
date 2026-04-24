#!/usr/bin/env python
from __future__ import annotations

import argparse
import logging
import os
from pathlib import Path
from typing import Sequence

from pygenomeviz import GenomeViz
from pygenomeviz.align import AlignCoord, MUMmer
from pygenomeviz.logger import init_logger
from pygenomeviz.parser import Genbank
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
from pygenomeviz.typing import PlotStyle, SeqType, TrackAlignType
from pygenomeviz.utils import is_pseudo_feature

CLI_NAME = "pgv-mummer"


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
    # MUMmer alignment options
    seqtype: SeqType,
    threads: int,
    length_thr: int,
    identity_thr: float,
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
    segment_space: float,
    feature_type2color: dict[str, str],
    pseudo_color: str,
    feature_plotstyle: PlotStyle,
    feature_linewidth: float,
    feature_labeltrack: str,
    feature_labeltype: str | None,
    feature_labelsize: int,
    cbar_width: float,
    cbar_height: float,
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
