from __future__ import annotations

import logging
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Sequence, get_args

from pygenomeviz.align import AlignCoord
from pygenomeviz.align.tool import AlignToolBase
from pygenomeviz.parser import Fasta, Genbank
from pygenomeviz.typing import SeqType

logger = logging.getLogger(__name__)


class Blast(AlignToolBase):
    """Blast Alignment Class"""

    def __init__(
        self,
        seqs: Sequence[str | Path | Fasta | Genbank],
        *,
        outdir: str | Path | None = None,
        seqtype: SeqType = "nucleotide",
        evalue: float = 1e-3,
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
        seqtype : SeqType, optional
            `nucleotide`(blastn) or `protein`(tblastx)
        evalue : float, optional
            E-value parameter for blast run
        threads : int | None, optional
            Threads parameter for blast run
        cmd_opts : str | None, optional
            `blastn` or `tblastx` additional command options
        """
        super().__init__()

        valid_seqtype = get_args(SeqType)
        if seqtype not in valid_seqtype:
            raise ValueError(f"{seqtype=} is invalid ({valid_seqtype=})")

        self._seqs = self._parse_input_gbk_and_fasta_seqs(seqs)
        self._outdir = None if outdir is None else Path(outdir)
        self._seqtype = seqtype
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
