from __future__ import annotations

import logging
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Sequence

from pygenomeviz.align import AlignCoord
from pygenomeviz.align.tool import AlignToolBase
from pygenomeviz.parser import Fasta, Genbank

logger = logging.getLogger(__name__)


class Last(AlignToolBase):
    """Last Alignment Class

    This class is experimental. API may change in the future release.
    """

    def __init__(
        self,
        seqs: Sequence[str | Path | Fasta | Genbank],
        *,
        outdir: str | Path | None = None,
        threads: int | None = None,
        cmd_opts: str | None = None,
    ):
        """
        Parameters
        ----------
        seqs : Sequence[str | Path | Fasta | Genbank]
            List of fasta or genbank
            (file suffix must be `.fa`, `.fna`, `.fasta`, `.gb`, `.gbk`, `.gbff`)
        outdir : str | Path | None, optional
            Temporary result directory. If None, tmp directory is auto created.
        threads : int | None, optional
            Threads parameter for lastal run
        cmd_opts : str | None, optional
            `lastal` additional command options
        """
        super().__init__()

        self._seqs = self._parse_input_gbk_and_fasta_seqs(seqs)
        self._outdir = None if outdir is None else Path(outdir)
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
