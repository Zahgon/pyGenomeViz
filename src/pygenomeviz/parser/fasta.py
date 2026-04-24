from __future__ import annotations

import bz2
import gzip
import zipfile
from io import TextIOWrapper
from pathlib import Path

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


class Fasta:
    """Fasta Parser Class"""

    def __init__(
        self,
        fasta: str | Path,
        *,
        name: str | None = None,
    ):
        """
        Parameters
        ----------
        fasta : str | Path
            Fasta file
        name : str | None, optional
            name (If None, file name is set)
        """
        fasta = Path(fasta)
        self._records = self._parse_fasta_file(fasta)

        # Set fasta name
        if name is not None:
            self._name = name
        else:
            if fasta.suffix in (".gz", ".bz2", ".zip"):
                self._name = fasta.with_suffix("").with_suffix("").name
            else:
                self._name = fasta.with_suffix("").name

        if len(self.records) == 0:
            raise ValueError(f"Failed to parse '{fasta}' as fasta file.")
        if len(self.records) != len(self.get_seqid2seq()):
            raise ValueError("Duplicate IDs are contained in fasta file.")

    ############################################################
    # Property
    ############################################################

    @property
    def name(self) -> str:
        """Name"""
        pass

    @property
    def records(self) -> list[SeqRecord]:
        """Fasta records"""
        pass

    @property
    def genome_seq(self) -> str:
        """Genome sequence (only first record)"""
        pass

    @property
    def genome_length(self) -> int:
        """Genome length (only first record)"""
        pass

    @property
    def full_genome_seq(self) -> str:
        """Full genome sequence (concatenate all records)"""
        pass

    @property
    def full_genome_length(self) -> int:
        """Full genome length (concatenate all records)"""
        pass

    ############################################################
    # Public Method
    ############################################################

    def get_seqid2seq(self) -> dict[str, str]:
        """Get seqid & complete/contig/scaffold genome sequence dict

        Returns
        -------
        seqid2seq : dict[str, str]
            seqid & genome sequence dict
        """
        pass

    def get_seqid2size(self) -> dict[str, int]:
        """Get seqid & complete/contig/scaffold genome size dict

        Returns
        -------
        seqid2size : dict[str, int]
            seqid & genome size dict
        """
        pass

    def get_seqid2record(self) -> dict[str, SeqRecord]:
        """Get seqid & complete/contig/scaffold genome record dict

        Returns
        -------
        seqid2record : dict[str, SeqRecord]
            seqi & genome record dict
        """
        pass

    def write_genome_fasta(self, outfile: str | Path) -> None:
        """Write genome fasta file

        Parameters
        ----------
        outfile : str | Path
            Output genome fasta file
        """
        pass

    ############################################################
    # Private Method
    ############################################################

    def _parse_fasta_file(self, fasta_file: str | Path) -> list[SeqRecord]:
        """Parse fasta file

        Parameters
        ----------
        fasta_file : str | Path
            Fasta file

        Returns
        -------
        seq_records : list[SeqRecord]
            SeqRecord list
        """
        pass
