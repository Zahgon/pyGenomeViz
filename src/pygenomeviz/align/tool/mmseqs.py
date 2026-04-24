from __future__ import annotations

import csv
import logging
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Sequence

from pygenomeviz.align import AlignCoord
from pygenomeviz.align.tool import AlignToolBase
from pygenomeviz.parser import Genbank

logger = logging.getLogger(__name__)


class MMseqs(AlignToolBase):
    """MMseqs RBH Search Class"""

    def __init__(
        self,
        seqs: Sequence[str | Path | Genbank],
        *,
        outdir: str | Path | None = None,
        evalue: float = 1e-3,
        threads: int | None = None,
        cmd_opts: str | None = None,
    ):
        """
        Parameters
        ----------
        seqs : Sequence[str | Path | Genbank]
            List of `genbank file` or `Genbank object`
        outdir : str | Path | None, optional
            Temporary result directory. If None, tmp directory is auto created.
        evalue : float, optional
            E-value parameter for MMseqs run
        threads : int | None, optional
            Threads parameter for MMseqs run
        cmd_opts : str | None, optional
            `mmseqs easy-rbh` additional command options
        """
        super().__init__()

        self._seqs = self._parse_input_gbk_seqs(seqs)
        self._outdir = None if outdir is None else Path(outdir)
        self._evalue = evalue
        self._threads = self.max_threads if threads is None else threads
        self._cmd_opts = cmd_opts

    @classmethod
    def get_tool_name(cls) -> str:
        """Tool name"""
        pass

    @classmethod
    def get_binary_names(cls) -> list[str]:
        """Binary names"""
        pass

    @classmethod
    def get_version(cls) -> str:
        """Tool version"""
        pass

    def run(self) -> list[AlignCoord]:
        """Run genome alignment"""
        pass

    def _write_cds_files(self, outdir: str | Path) -> list[Path]:
        """Write CDS files"""
        pass

    def _parse_coords_file(
        self,
        rbh_result_file: str | Path,
        query_id: str,
        ref_id: str,
    ) -> list[AlignCoord]:
        """Parse MMseqs RBH result

        Parameters
        ----------
        rbh_result_file : str | Path
            MMseqs RBH result file
        query_id : str
            Query ID
        ref_id : str
            Reference ID

        Returns
        -------
        align_coords : list[AlignCoord]
            Align Coords
        """
        pass
