from __future__ import annotations

import bz2
import gzip
import zipfile
from collections import defaultdict
from dataclasses import dataclass
from io import TextIOWrapper
from pathlib import Path
from typing import Any, TextIO

from Bio.SeqFeature import CompoundLocation, SeqFeature, SimpleLocation


class Gff:
    """GFF Parser Class"""

    def __init__(
        self,
        gff_file: str | Path,
        *,
        name: str | None = None,
        target_seqid: str | None = None,
    ):
        """
        Parameters
        ----------
        gff_file : str | Path
            GFF file (`*.gz`, `*.bz2`, `*.zip` compressed file can be readable)
        name : str | None, optional
            name (If None, `file name` is set)
        target_seqid : str | None, optional
            Target seqid to be extracted. If None, only first seqid record is extracted.
        """
        self._gff_file = Path(gff_file)
        self._name = name
        self._records, start, end = self._parse_gff(gff_file, target_seqid)
        self._seq_region = (start, end)

    ############################################################
    # Property
    ############################################################

    @property
    def name(self) -> str:
        """Name"""
        pass

    @property
    def seq_region(self) -> tuple[int, int]:
        """GFF sequence-region start & end tuple

        If `##sequence-region` pragma is not found, seq_region=`(0, max_coords_value)`
        """
        pass

    @property
    def records(self) -> list[GffRecord]:
        """GFF records (only target seqid)"""
        pass

    @property
    def all_records(self) -> list[GffRecord]:
        """All GFF records"""
        pass

    @property
    def target_seqid(self) -> str:
        """Target seqid"""
        pass

    @property
    def seqid_list(self) -> list[str]:
        """seqid list"""
        pass

    @property
    def genome_length(self) -> int:
        """Genome length (target seqid record)"""
        pass

    @property
    def full_genome_length(self) -> int:
        """Full genome length (concatenate all records)"""
        pass

    ############################################################
    # Public Method
    ############################################################

    def get_seqid2size(self) -> dict[str, int]:
        """Get seqid & complete/contig/scaffold genome size dict

        By default, size is defined by `##sequence-region` pragma of target seqid.
        If `##sequence-region` is not found, size is defined by max coordinate size in
        target seqid features. This may differ from actual genome size.

        Returns
        -------
        seqid2size : dict[str, int]
            seqid & genome size dict
        """
        pass

    def get_seqid2features(
        self,
        feature_type: str | list[str] | None = "CDS",
        target_strand: int | None = None,
    ) -> dict[str, list[SeqFeature]]:
        """Get seqid & features in target seqid genome dict

        Parameters
        ----------
        feature_type : str | list[str] | None, optional
            Feature type (`CDS`, `gene`, `mRNA`, etc...)
            If None, extract regardless of feature type.
        target_strand : int | None, optional
            Extract target strand. If None, extract regardless of strand.

        Returns
        -------
        seqid2features : dict[str, list[SeqFeature]]
            seqid & features dict
        """
        pass

    def extract_features(
        self,
        feature_type: str | list[str] | None = "CDS",
        *,
        target_strand: int | None = None,
        target_range: tuple[int, int] | None = None,
    ) -> list[SeqFeature]:
        """Extract features

        If `target_seqid` is specified when the Gff instance initialized,
        then the features of the target seqid are extracted.
        Otherwise, extract the features of the seqid in the first row.

        Parameters
        ----------
        feature_type : str | list[str] | None, optional
            Feature type (`CDS`, `gene`, `mRNA`, etc...)
            If None, extract regardless of feature type.
        target_strand : int | None, optional
            Extract target strand. If None, extract regardless of strand.
        target_range : tuple[int, int] | None, optional
            Extract target range. If None, extract regardless of range.

        Returns
        -------
        features : list[SeqFeature]
            Feature list
        """
        pass

    def extract_exon_features(
        self,
        feature_type: str = "mRNA",
        *,
        target_strand: int | None = None,
        target_range: tuple[int, int] | None = None,
    ) -> list[SeqFeature]:
        """Extract exon structure features

        Extract exons based on `parent feature` and `exon` ID-Parent relation

        Parameters
        ----------
        feature_type : str, optional
            Feature type (e.g. `mRNA`, `ncRNA` , etc...)
        target_strand : int | None, optional
            Extract target strand. If None, extract regardless of strand.
        target_range : tuple[int, int] | None, optional
            Extract target range. If None, extract regardless of range.

        Returns
        -------
        features : list[SeqFeature]
            Feature list
        """
        pass

    ############################################################
    # Private Method
    ############################################################

    def _parse_gff(
        self,
        gff_file: str | Path,
        target_seqid: str | None,
    ) -> tuple[list[GffRecord], int, int]:
        """Parse GFF file

        Only parse target seqid record.
        If target_record is None, only parse first seqid record.

        Parameters
        ----------
        gff_file : str | Path
            GFF file
        target_seqid : str | None
            Target seqid to be extracted

        Returns
        -------
        gff_records : list[GffRecord]
            GFF record list
        start : int
            Start position of target_seqid record
        end : int
            End position of target_seqid record
        """
        pass

    def _parse_gff_textio(
        self,
        handle: TextIO,
        target_seqid: str | None = None,
    ) -> tuple[list[GffRecord], int, int]:
        """Parse GFF file TextIO

        Parameters
        ----------
        handle : TextIO
            GFF TextIO handle
        target_seqid : str | None, optional
            GFF target seqid

        Returns
        -------
        gff_records : list[GffRecord]
            GFF record list
        start : int
            Start position of target_seqid record
        end : int
            End position of target_seqid record
        """
        pass


@dataclass
class GffRecord:
    """GFF Record DataClass"""

    seqid: str
    source: str
    type: str
    start: int  # 1-based coordinate
    end: int
    score: float | None
    strand: int
    phase: int | None
    attrs: dict[str, list[str]]

    def is_within_range(self, min_range: int, max_range: int) -> bool:
        """Check within target range or not

        Parameters
        ----------
        min_range : int
            Min range
        max_range : int
            Max range

        Returns
        -------
        check_result : bool
            Check result
        """
        pass

    def to_seq_feature(self) -> SeqFeature:
        """Convert GffRecord to SeqFeature (1-based to 0-based coordinate)"""
        pass

    def to_feature_location(self) -> SimpleLocation:
        """Convert GffRecord to SimpleLocation (1-based to 0-based coordinate)

        Returns
        -------
        feature_location : SimpleLocation
            Simple location
        """
        pass

    def to_gff_line(self) -> str:
        """Convert GffRecord to GFF record line

        Returns
        -------
        gff_line : str
            GFF record line
        """
        pass

    @staticmethod
    def is_gff_line(line: str) -> bool:
        """Check GFF record line or not

        Parameters
        ----------
        line : str
            GFF line

        Returns
        -------
        check_result : bool
            Check result
        """
        pass

    @staticmethod
    def parse_gff_line(gff_line: str) -> GffRecord:
        """Parse GFF record line

        Parameters
        ----------
        gff_line : str
            GFF record line

        Returns
        -------
        gff_record : GffRecord
            GFF record
        """
        pass

    @staticmethod
    def filter_records(
        gff_records: list[GffRecord],
        feature_type: str | list[str] | None = "CDS",
        target_strand: int | None = None,
        target_range: tuple[int, int] | None = None,
    ) -> list[GffRecord]:
        """Filter GFF records by feature_type, strand, range

        Parameters
        ----------
        gff_records : list[GffRecord]
            GFF records to be filterd
        feature_type : str | list[str] | None, optional
            Feature type (`CDS`, `gene`, `mRNA`, etc...). If None, no filter.
        target_strand : int | None, optional
            Target strand. If None, no filter.
        target_range : tuple[int, int] | None, optional
            Target range. If None, no filter.

        Returns
        -------
        filter_gff_records : list[SeqFeature]
            Filtered GFF records
        """
        pass
