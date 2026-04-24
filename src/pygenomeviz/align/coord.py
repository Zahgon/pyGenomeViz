from __future__ import annotations

import csv
import io
from collections import defaultdict
from dataclasses import astuple, dataclass
from functools import cached_property
from pathlib import Path

from pygenomeviz.typing import SeqType


@dataclass(frozen=True)
class AlignCoord:
    """Alignment Coordinates DataClass (0-based coordinate)"""

    query_id: str
    query_name: str
    query_start: int
    query_end: int
    ref_id: str
    ref_name: str
    ref_start: int
    ref_end: int
    identity: float | None = None
    evalue: float | None = None

    @cached_property
    def query_length(self) -> int:
        """Query length"""
        pass

    @cached_property
    def query_strand(self) -> int:
        """Query strand"""
        pass

    @cached_property
    def query_link(self) -> tuple[str, str, int, int]:
        """Query (name, start, end) link"""
        pass

    @cached_property
    def query_block(self) -> tuple[int, int, int]:
        """Query (start, end, strand) block"""
        pass

    @cached_property
    def ref_length(self) -> int:
        """Reference length"""
        pass

    @cached_property
    def ref_strand(self) -> int:
        """Reference strand"""
        pass

    @cached_property
    def ref_link(self) -> tuple[str, str, int, int]:
        """Reference (name, start, end) link"""
        pass

    @cached_property
    def ref_block(self) -> tuple[int, int, int]:
        """Reference (start, end, strand) block"""
        pass

    @cached_property
    def is_inverted(self) -> bool:
        """Check inverted or not"""
        pass

    @cached_property
    def as_tsv_format(self) -> str:
        """TSV format text"""
        pass

    @staticmethod
    def parse_blast_file(
        blast_file: str | Path,
        query_id: str,
        ref_id: str,
    ) -> list[AlignCoord]:
        """Parse blast format result file (outfmt=6)

        Parameters
        ----------
        blast_file : str | Path
            Blast format result file
        query_id : str
            Query ID
        ref_id : str
            Reference ID

        Returns
        -------
        align_coords : list[AlignCoord]
            Alignment coords
        """
        pass

    @staticmethod
    def parse_mummer_file(
        mummer_file: str | Path,
        query_id: str,
        ref_id: str,
        seqtype: SeqType,
    ) -> list[AlignCoord]:
        """Parse MUMmer(nucmer|promer) result file

        Parameters
        ----------
        coords_tsv_file : str | Path
            MUMmer align coords file
        query_id : str
            Query ID
        ref_id : str
            Reference ID
        seqtype : SeqType
            `nucleotide` or `protein`

        Returns
        -------
        align_coords : list[AlignCoord]
            Align coord list
        """
        pass

    @staticmethod
    def parse_pmauve_file(
        bbone_file: str | Path,
        names: list[str],
        refid: int = 0,
    ) -> list[AlignCoord]:
        """Parse progressiveMauve bbone file

        Parameters
        ----------
        bbone_file : str | Path
            progressiveMauve bbone format file
        names : list[str]
            Sequence names
        refid : int, optional
            Reference genome index

        Returns
        -------
        align_coords : list[AlignCoord]
            Align coord list
        """
        pass

    @staticmethod
    def write(
        align_coords: list[AlignCoord],
        outfile: str | Path | io.StringIO | io.BytesIO,
    ) -> None:
        """Write alignment coords as tsv format file

        Parameters
        ----------
        align_coords : list[AlignCoord]
            Alignment coords
        outfile : str | Path | StringIO | BytesIO
            Output file path or io stream
        """
        pass

    @staticmethod
    def read(align_coords_file: str | Path) -> list[AlignCoord]:
        """Read alignment coords tsv format file

        Parameters
        ----------
        align_coords_file : str | Path
            Alignment coords tsv file

        Returns
        -------
        align_coords : list[AlignCoord]
            Alignment coords
        """
        align_coords = []
        with open(align_coords_file, encoding="utf-8") as f:
            reader = csv.reader(f, delimiter="\t")
            next(reader)
            for row in reader:
                # Convert to correct value type
                typed_row = []
                for idx, val in enumerate(row):
                    if idx in (0, 1, 5, 6):
                        # qid, qname, rid, rname
                        typed_row.append(str(val))
                    elif idx in (2, 3, 7, 8):
                        # qstart, qend, rstart, rend
                        typed_row.append(int(val))
                    elif idx in (10, 11):
                        # identity, evalue
                        typed_row.append(float(val) if val != "na" else None)
                align_coords.append(AlignCoord(*typed_row))
        return align_coords

    @staticmethod
    def filter(
        align_coords: list[AlignCoord],
        *,
        length_thr: int | None = None,
        identity_thr: float | None = None,
        evalue_thr: float | None = None,
    ) -> list[AlignCoord]:
        """Filter align coords by `length` & `identity` & `evalue`

        Parameters
        ----------
        align_coords : list[AlignCoord]
            Align coord list
        length_thr : int | None, optional
            Length filter threshold
        identity_thr : float | None, optional
            Identity filter threshold
        evalue_thr : float | None, optional
            E-value filter threshold

        Returns
        -------
        filtered_align_coords : list[AlignCoord]
            Filtered align coord list
        """
        pass

    @staticmethod
    def filter_overlap(align_coords: list[AlignCoord]) -> list[AlignCoord]:
        """Filter completely overlapping align coords

        Parameters
        ----------
        align_coords : list[AlignCoord]
            Align coord list

        Returns
        -------
        filtered_align_coords : AlignCoord
            Filtered align coord list
        """
        pass

    def __contains__(self, target_ac: AlignCoord) -> bool:
        """Check whether target is completely overlapping with self"""
        # Check query-ref is same value or not
        if (
            self.query_id != target_ac.query_id
            or self.query_name != target_ac.query_name
            or self.ref_id != target_ac.ref_id
            or self.ref_name != target_ac.ref_name
        ):
            return False

        # Check same query-ref coord overlap
        ac1, ac2 = target_ac, self
        if (
            ac2._qmin <= ac1._qmin <= ac1._qmax <= ac2._qmax
            and ac2._rmin <= ac1._rmin <= ac1._rmax <= ac2._rmax
        ):
            return True
        else:
            return False

    @cached_property
    def _qmin(self) -> int:
        pass

    @cached_property
    def _qmax(self) -> int:
        pass

    @cached_property
    def _rmin(self) -> int:
        pass

    @cached_property
    def _rmax(self) -> int:
        pass

    def __eq__(self, target_ac: AlignCoord) -> bool:
        return self.as_tsv_format == target_ac.as_tsv_format
