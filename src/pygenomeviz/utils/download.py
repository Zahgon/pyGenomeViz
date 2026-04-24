from __future__ import annotations

import logging
import os
from io import StringIO, TextIOWrapper
from pathlib import Path
from urllib.request import urlretrieve

from Bio import Entrez

from pygenomeviz.parser import Genbank
from pygenomeviz.typing import GenbankDatasetName, GffExampleFileName

GITHUB_DATA_URL = "https://raw.githubusercontent.com/moshi4/pygenomeviz-data-v1/main/"

GBK_DATASET = {
    "acinetobacter_phage": [
        "NC_049491.gbk",
        "NC_049492.gbk",
        "NC_049493.gbk",
        "NC_049494.gbk",
    ],
    "yersinia_phage": [
        "NC_070914.gbk",
        "NC_070915.gbk",
        "NC_070916.gbk",
        "NC_070918.gbk",
    ],
    "enterobacteria_phage": [
        "NC_013600.gbk",
        "NC_016566.gbk",
        "NC_019724.gbk",
        "NC_024783.gbk",
        "NC_028901.gbk",
        "NC_031081.gbk",
    ],
    "mycoplasma_mycoides": [
        "GCF_000023685.1.gbff",
        "GCF_000800785.1.gbff",
        "GCF_000959055.1.gbff",
        "GCF_000959065.1.gbff",
    ],
    "escherichia_coli": [
        "NC_000913.gbk.gz",
        "NC_002695.gbk.gz",
        "NC_011751.gbk.gz",
        "NC_011750.gbk.gz",
    ],
    "saccharomyces": [
        "Saccharomyces_cerevisiae.gbff.gz",
        "Saccharomyces_kudriavzevii.gbff.gz",
        "Saccharomyces_mikatae.gbff.gz",
    ],
}

GFF_FILES = [
    "enterobacteria_phage.gff",
    "mycoplasma_mycoides.gff",
    "escherichia_coli.gff.gz",
    "saccharomyces_cerevisiae.gff.gz",
]


def load_example_fasta_dataset(
    name: GenbankDatasetName,
    *,
    cache_dir: str | Path | None = None,
    overwrite_cache: bool = False,
) -> list[Path]:
    """Load pygenomeviz example fasta dataset

    Load genbank datasets from <https://github.com/moshi4/pygenomeviz-data-v1>
    and convert genbank to fasta format.
    Cache datasets in local directory (Default: `~/.cache/pygenomeviz/`).

    List of dataset name

    - `acinetobacter_phage` (4 species)
    - `yersinia_phage` (4 species)
    - `enterobacteria_phage` (6 species)
    - `mycoplasma_mycoides` (4 species)
    - `escherichia_coli` (4 species, gzip compressed)
    - `saccharomyces` (3 species, gzip compressed)

    Parameters
    ----------
    name : str
        Dataset name (e.g. `enterobacteria_phage`)
    cache_dir : str | Path | None, optional
        Output cache directory (Default: `~/.cache/pygenomeviz/`)
    overwrite_cache : bool, optional
        If True, overwrite cached dataset
    quiet : bool, optional
        If True, no print log on screen.

    Returns
    -------
    fasta_files : list[Path]
        Fasta files
    """
    pass


def load_example_genbank_dataset(
    name: GenbankDatasetName,
    *,
    cache_dir: str | Path | None = None,
    overwrite_cache: bool = False,
) -> list[Path]:
    """Load pygenomeviz example genbank dataset

    Load genbank datasets from <https://github.com/moshi4/pygenomeviz-data-v1>
    and cache datasets in local directory (Default: `~/.cache/pygenomeviz/`).

    List of dataset name

    - `acinetobacter_phage` (4 species)
    - `yersinia_phage` (4 species)
    - `enterobacteria_phage` (6 species)
    - `mycoplasma_mycoides` (4 species)
    - `escherichia_coli` (4 species, gzip compressed)
    - `saccharomyces` (3 species, gzip compressed)

    Parameters
    ----------
    name : str
        Dataset name (e.g. `enterobacteria_phage`)
    cache_dir : str | Path | None, optional
        Output cache directory (Default: `~/.cache/pygenomeviz/`)
    overwrite_cache : bool, optional
        If True, overwrite cached dataset

    Returns
    -------
    gbk_files : list[Path]
        Genbank files
    """
    pass


def load_example_gff_file(
    filename: GffExampleFileName,
    *,
    cache_dir: str | Path | None = None,
    overwrite_cache: bool = False,
) -> Path:
    """Load pygenomeviz example GFF file

    Load example GFF file from <https://github.com/moshi4/pygenomeviz-data-v1/>
    and cache GFF file in local directory (Default: `~/.cache/pygenomeviz/`).

    List of example GFF filename

    - `enterobacteria_phage.gff`
    - `mycoplasma_mycoides.gff`
    - `escherichia_coli.gff.gz`
    - `saccharomyces_cerevisiae.gff.gz`

    Parameters
    ----------
    filename : str
        GFF filename (e.g. `enterobacteria_phage.gff`)
    cache_dir : str | Path | None, optional
        Output cache directory (Default: `~/.cache/pygenomeviz/`)
    overwrite_cache : bool, optional
        If True, overwrite cached GFF file

    Returns
    -------
    gff_file : Path
        GFF file
    """
    pass


def fetch_genbank_by_accid(
    accid: str,
    gbk_outfile: str | Path | None = None,
    email: str | None = None,
) -> TextIOWrapper:
    """Fetch genbank text by 'Accession ID'

    Parameters
    ----------
    accid : str
        Accession ID
    gbk_outfile : str | Path | None, optional
        If file path is set, write fetch data to file
    email : str | None, optional
        Email address to notify download limitation (Required for bulk download)

    Returns
    -------
    TextIOWrapper
        Genbank data

    Examples
    --------
    >>> gbk_text = fetch_genbank_by_accid("NC_013600")
    >>> gbk = Genbank(gbk_text)
    """
    pass
