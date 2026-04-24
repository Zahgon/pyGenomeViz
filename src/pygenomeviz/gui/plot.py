from __future__ import annotations

import hashlib
import os
from pathlib import Path

from pygenomeviz import GenomeViz
from pygenomeviz.align import AlignCoord, Blast, MMseqs, MUMmer
from pygenomeviz.exception import SegmentNotFoundError
from pygenomeviz.gui import config, utils
from pygenomeviz.parser import Genbank
from pygenomeviz.utils import is_pseudo_feature


def plot_by_gui_cfg(
    gbk_list: list[Genbank],
    cfg: config.PgvGuiPlotConfig,
) -> tuple[GenomeViz, list[AlignCoord]]:
    """Plot by GUI configs

    Parameters
    ----------
    gbk_list : list[Genbank]
        Genbank list
    cfg : PgvConfig
        Config

    Returns
    -------
    gv : GenomeViz
        GenomeViz instance
    align_coords : list[AlignCoord]
        AlignCoord list
    """
    pass
