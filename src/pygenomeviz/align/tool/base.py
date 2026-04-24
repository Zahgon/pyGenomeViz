from __future__ import annotations

import logging
import os
import re
import shlex
import shutil
import subprocess as sp
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Sequence

from pygenomeviz.align import AlignCoord
from pygenomeviz.const import UNKNOWN_VERSION
from pygenomeviz.parser import Fasta, Genbank

logger = logging.getLogger(__name__)


class AlignToolBase(ABC):
    """Alignment Tool Abstract Base Class"""

    def __init__(self):
        self.check_installation()

    @property
    def max_threads(self) -> int:
        """Max threads number"""
        pass

    @classmethod
    @abstractmethod
    def get_tool_name(cls) -> str:
        """Tool name"""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_binary_names(cls) -> list[str]:
        """Binary names"""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_version(cls) -> str:
        """Tool version"""
        raise NotImplementedError

    @abstractmethod
    def run(self) -> list[AlignCoord]:
        """Run genome alignment"""
        raise NotImplementedError

    @classmethod
    def check_installation(
        cls,
        exit_on_false: bool = True,
    ) -> bool:
        """Check required binaries installation

        Parameters
        ----------
        exit_on_false : bool, optional
            If True and check result is False, raise RuntimeError.

        Returns
        -------
        result : bool
            Check result
        """
        pass

    def run_cmd(
        self,
        cmd: str,
        stdout_file: str | Path | None = None,
    ) -> None:
        """Run command

        Parameters
        ----------
        cmd : str
            Command to run
        stdout_file : str | Path | None, optional
            Write stdout result if file is set
        """
        pass

    @classmethod
    def _get_version(cls, cmd: str, pattern: str) -> str:
        """Get tool version by cmd & regex pattern

        Parameters
        ----------
        cmd : str
            Command to get version info
        pattern : str
            Regex pattern for search version

        Returns
        -------
        version : str
            Tool version (e.g. `v1.2.3`)
        """
        pass

    def _parse_input_gbk_seqs(
        self, seqs: Sequence[str | Path | Genbank]
    ) -> list[Genbank]:
        """Parse input genbank sequences

        Parameters
        ----------
        seqs : Sequence[str | Path | Genbank]
            List of `genbank file` or `Genbank object`

        Returns
        -------
        parse_seqs : list[Genbank]
            List of `Genbank object`
        """
        pass

    def _parse_input_gbk_and_fasta_seqs(
        self, seqs: Sequence[str | Path | Fasta | Genbank]
    ) -> Sequence[Fasta | Genbank]:
        """Parse input genbank and fasta sequences

        Parameters
        ----------
        seqs : Sequence[str | Path | Fasta | Genbank]
            List of fasta or genbank

        Returns
        -------
        parse_seqs : Sequence[Fasta | Genbank]
            List of fasta or genbank
        """
        pass

    def _write_genome_files(
        self,
        seqs: Sequence[Fasta | Genbank],
        outdir: str | Path,
    ) -> list[Path]:
        """Write genome fasta files to output directory

        Parameters
        ----------
        seqs : Sequence[Fasta | Genbank]
            List of fasta or genbank
        outdir : str | Path
            Target output directory

        Returns
        -------
        genome_files : list[Path]
            Genome fasta files
        """
        pass
