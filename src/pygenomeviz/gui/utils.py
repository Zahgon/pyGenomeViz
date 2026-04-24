from __future__ import annotations

import gzip
import io
import time
from collections import defaultdict
from io import StringIO
from pathlib import Path
from typing import TYPE_CHECKING

import streamlit as st
from Bio.SeqFeature import SeqFeature
from matplotlib.figure import Figure

from pygenomeviz import GenomeViz
from pygenomeviz.parser import Genbank

if TYPE_CHECKING:
    from streamlit.runtime.uploaded_file_manager import UploadedFile


@st.cache_data(ttl=3600)
def load_gbk_file(gbk_file: str | Path | UploadedFile) -> Genbank:
    """Load genbank file

    Parameters
    ----------
    gbk_file : str | Path | UploadedFile
        Genbank file

    Returns
    -------
    gbk : Genbank
        Genbank parse object
    """
    pass


def is_st_cloud() -> bool:
    """Is launch on streamlit cloud"""
    pass


def remove_old_files(target_dir: Path, ttl: int = 3600) -> None:
    """Remove old file in target directory

    Parameters
    ----------
    target_dir : Path
        Target directory path
    ttl : int, optional
        Time to live
    """
    pass


def extract_all_feature_types(gbk_list: list[Genbank], sort: bool = True) -> list[str]:
    """Extract all feature types from genbank list

    Parameters
    ----------
    gbk_list : list[Genbank]
        Genbank object list
    sort : bool, optional
        Sort feature types (`CDS`, `rRNA`, `tRNA`, ...)

    Returns
    -------
    all_feature_types : list[str]
        All feature types
    """
    pass


def get_features_count_label(features: list[SeqFeature]) -> str:
    """Get features count label

    Parameters
    ----------
    features : list[SeqFeature]
        Target features

    Returns
    -------
    label : str
        Count label
    """
    pass


def get_fig_bytes(gv: GenomeViz, fig: Figure, format: str) -> io.BytesIO:
    """Get figure bytes"""
    pass
