from __future__ import annotations

import uuid
from copy import deepcopy
from typing import TYPE_CHECKING, Any, Callable, overload

import numpy as np
from Bio.SeqFeature import CompoundLocation, SeqFeature, SimpleLocation

from pygenomeviz.exception import FeatureRangeError
from pygenomeviz.typing import HPos, PlotStyle, VPos

if TYPE_CHECKING:
    from numpy.typing import NDArray

    from pygenomeviz.track import FeatureTrack


class FeatureSegment:
    """Feature Segment Class"""

    def __init__(
        self,
        name: str,
        start: int,
        end: int,
        feature_track: FeatureTrack,
    ):
        """
        Parameters
        ----------
        name : str
            Segment name
        start : int
            Segment start position
        end : int
            Segment end position
        feature_track : FeatureTrack
            Parent feature track
        """
        self._name = name
        self._start = start
        self._end = end
        self._feature_track = feature_track

        self._features: list[SeqFeature] = []
        self._exon_features: list[SeqFeature] = []
        self._text_kws_list: list[dict[str, Any]] = []
        self._gid2feature_dict: dict[str, dict[str, Any]] = {}

    ############################################################
    # Property
    ############################################################

    @property
    def name(self) -> str:
        """Segment name"""
        pass

    @property
    def start(self) -> int:
        """Segment start position"""
        pass

    @property
    def end(self) -> int:
        """Segment end position"""
        pass

    @property
    def range(self) -> tuple[int, int]:
        """Segment (start, end) range"""
        pass

    @property
    def size(self) -> int:
        """Segment size"""
        pass

    @property
    def feature_track(self) -> FeatureTrack:
        """Parent feature track"""
        pass

    @property
    def track_start(self) -> int:
        """Segment start position in track"""
        pass

    @property
    def track_end(self) -> int:
        """Segment end position in track"""
        pass

    @property
    def gid2feature_dict(self) -> dict[str, dict[str, Any]]:
        """gid & feature dict (Sort by start coordinate)"""
        pass

    @property
    def transform_features(self) -> list[SeqFeature]:
        """Coordinate transformed features

        Segment-level coordinate is transformed to track-level coordinate.
        """
        pass

    @property
    def transform_exon_features(self) -> list[SeqFeature]:
        """Coordinate transformed exon features

        Segment-level coordinate is transformed to track-level coordinate.
        """
        pass

    @property
    def transform_text_kws_list(self) -> list[dict[str, Any]]:
        """Coordinate transformed text keywords list"""
        pass

    ############################################################
    # Public Method
    ############################################################

    def is_within_range(self, pos: int | tuple[int, int]) -> bool:
        """Check target pos is within segment range"""
        pass

    @overload
    def transform_coord(self, x: int) -> int: ...
    @overload
    def transform_coord(self, x: float) -> float: ...
    @overload
    def transform_coord(self, x: NDArray) -> NDArray[np.float64]: ...

    def transform_coord(
        self, x: int | float | NDArray
    ) -> int | float | NDArray[np.float64]:
        """Transform segment-level coordinate to track-level coordinate

        Parameters
        ----------
        x : int | float| NDArray
            Segment level coordinate(s)

        Returns
        -------
        track_coord : int | float | NDArray[np.float64]
            Track level coordinate(s)
        """
        pass

    def add_text(
        self,
        x: float,
        text: str,
        *,
        size: float = 12,
        vpos: VPos = "top",
        hpos: HPos = "left",
        ymargin: float = 0.2,
        rotation: float = 45,
        **kwargs,
    ) -> None:
        """Add text

        Parameters
        ----------
        x : float
            Text x coordinate
        text : str
            Text content
        size : float, optional
            Text size
        vpos : str, optional
            Vertical position (`top`|`center`|`bottom`)
        hpos : str, optional
            Horizontal position (`left`|`center`|`right`)
        ymargin : float, optional
            Y margin
        rotation : float, optional
            Text rotation
        **kwargs : dict, optional
            Text properties (e.g. `color="red", ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html>
        """
        pass

    def add_sublabel(
        self,
        text: str | None = None,
        *,
        size: float = 12,
        pos: str = "bottom-left",
        ymargin: float = 0.2,
        rotation: float = 0,
        **kwargs,
    ) -> None:
        """Add sublabel

        Parameters
        ----------
        text : str | None, optional
            Text content. If None, `{start:,} - {end:,} bp` label is set.
        size : float, optional
            Text size
        pos : str, optional
            Label position ([`top`|`bottom`]-[`left`|`center`|`right`])
        ymargin : float, optional
            Y margin
        rotation : float, optional
            Text rotation
        **kwargs : dict, optional
            `segment.add_text()` method keyword arguments (e.g. `color="red", ...`)
        """
        pass

    def add_feature(
        self,
        start: int,
        end: int,
        strand: int = 1,
        *,
        plotstyle: PlotStyle = "arrow",
        arrow_shaft_ratio: float = 0.5,
        extra_tooltip: dict[str, str] | None = None,
        label: str = "",
        text_kws: dict[str, Any] | None = None,
        **kwargs,
    ) -> None:
        """Add feature

        Parameters
        ----------
        start : int
            Start position
        end : int
            End position
        strand : int, optional
            Feature strand
        plotstyle : PlotStyle, optional
            Feature plot style (`bigarrow`|`arrow`|`bigbox`|`box`|`bigrbox`|`rbox`)
        arrow_shaft_ratio : float, optional
            Arrow shaft size ratio
        extra_tooltip : dict[str, str] | None, optional
            Extra tooltip dict for html figure
        label : str, optional
            Feature label text
        text_kws : dict[str, Any] | None, optional
            `segment.add_text()` method keyword arguments
            (e.g. `dict(size=12, color="red", ...)`)
        **kwargs : dict, optional
            Patch properties (e.g. `fc="red", lw=0.5, hatch="//", ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        """
        pass

    def add_features(
        self,
        features: SeqFeature | list[SeqFeature],
        *,
        plotstyle: PlotStyle = "arrow",
        arrow_shaft_ratio: float = 0.5,
        label_type: str | None = None,
        label_handler: Callable[[str], str] | None = None,
        extra_tooltip: dict[str, str] | None = None,
        ignore_outside_range: bool = False,
        text_kws: dict[str, Any] | None = None,
        **kwargs,
    ) -> None:
        """Add features (BioPython SeqFeature)

        Parameters
        ----------
        features : SeqFeature | list[SeqFeature]
            BioPython SeqFeature or SeqFeature list
        plotstyle : PlotStyle, optional
            Feature plot style (`bigarrow`|`arrow`|`bigbox`|`box`|`bigrbox`|`rbox`)
        arrow_shaft_ratio : float, optional
            Arrow shaft size ratio
        label_type : str | None, optional
            Label type (e.g. `gene`,`protein_id`,`product`, etc...)
        label_handler : Callable[[str], str] | None, optional
            Label handler function to customize label display.
            If None, set label handler to exclude labels containing `hypothetical`.
        extra_tooltip : dict[str, str] | None, optional
            Extra tooltip dict for html figure
        ignore_outside_range : bool, optional
            If True and the feature position is outside the range of the track segment,
            ignore it without raising an error.
        text_kws : dict[str, Any] | None, optional
            `segment.add_text()` method keyword arguments
            (e.g. `dict(color="red", ...)`)
        **kwargs : dict, optional
            Patch properties (e.g. `fc="red", lw=0.5, hatch="//", ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        """
        pass

    def add_exon_feature(
        self,
        locs: list[tuple[int, int]],
        strand: int = 1,
        *,
        plotstyle: PlotStyle = "arrow",
        arrow_shaft_ratio: float = 0.5,
        label: str = "",
        patch_kws: dict[str, Any] | None = None,
        intron_patch_kws: dict[str, Any] | None = None,
        text_kws: dict[str, Any] | None = None,
    ) -> None:
        """Add exon feature

        Parameters
        ----------
        locs : list[tuple[int, int]]
            Exon locations (e.g. `[(0, 100), (200, 300), (350, 400)]`)
        strand : int, optional
            Feature strand
        plotstyle : PlotStyle, optional
            Feature plot style (`bigarrow`|`arrow`|`bigbox`|`box`|`bigrbox`|`rbox`)
        arrow_shaft_ratio : float, optional
            Arrow shaft size ratio
        label : str, optional
            Feature label
        patch_kws : dict[str, Any] | None, optional
            Exon patch properties (e.g. `dict(fc="red", lw=0.5, hatch="//", ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        intron_patch_kws : dict[str, Any] | None, optional
            Intron patch properties (e.g. `dict(color="red", lw=2.0, ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        text_kws : dict[str, Any] | None, optional
            `segment.add_text()` method keyword arguments
            (e.g. `dict(size=12, color="red", ...)`)
        """
        pass

    def add_exon_features(
        self,
        features: SeqFeature | list[SeqFeature],
        *,
        plotstyle: PlotStyle = "arrow",
        arrow_shaft_ratio: float = 0.5,
        label_type: str | None = None,
        label_handler: Callable[[str], str] | None = None,
        extra_tooltip: dict[str, str] | None = None,
        ignore_outside_range: bool = False,
        patch_kws: dict[str, Any] | None = None,
        intron_patch_kws: dict[str, Any] | None = None,
        text_kws: dict[str, Any] | None = None,
    ) -> None:
        """Add exon features (BioPython SeqFeature)

        Parameters
        ----------
        features : SeqFeature | list[SeqFeature]
            BioPython SeqFeature or SeqFeature list
        plotstyle : PlotStyle, optional
            Feature plot style (`bigarrow`|`arrow`|`bigbox`|`box`|`bigrbox`|`rbox`)
        arrow_shaft_ratio : float, optional
            Arrow shaft size ratio
        label_type : str | None, optional
            Label type (e.g. `gene`,`protein_id`,`product`, etc...)
        label_handler : Callable[[str], str] | None, optional
            Label handler function to customize label display.
            If None, set label handler to exclude labels containing `hypothetical`.
        extra_tooltip : dict[str, str] | None, optional
            Extra tooltip dict for html figure
        ignore_outside_range : bool, optional
            If True and the feature position is outside the range of the track segment,
            ignore it without raising an error.
        patch_kws : dict[str, Any] | None, optional
            Exon patch properties (e.g. `dict(fc="red", lw=0.5, hatch="//", ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        intron_patch_kws : dict[str, Any] | None, optional
            Intron patch properties (e.g. `dict(color="red", lw=2.0, ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        text_kws : dict[str, Any] | None, optional
            `segment.add_text()` method keyword arguments
            (e.g. `dict(size=12, color="red", ...)`)
        """
        pass

    ############################################################
    # Private Method
    ############################################################

    def _check_feature_within_segment(self, feature: SeqFeature) -> None:
        """Check if feature is within segment

        Parameters
        ----------
        feature : SeqFeature
            BioPython SeqFeature

        Raises
        ------
        FeatureOutsideRangeError
            feature is not within segment range
        """
        pass

    def _transform_feature(self, feature: SeqFeature) -> SeqFeature:
        """Transform segment-level feature coordinate to track-level

        Parameters
        ----------
        feature : SeqFeature
            BioPython SeqFeature

        Returns
        -------
        feature : SeqFeature
            Transformaed feature
        """
        pass

    def _add_gid2feature_dict(
        self,
        gid: str,
        feature: SeqFeature,
        extra_tooltip: dict[str, str] | None = None,
    ) -> None:
        """Add gid & feature dict

        Parameters
        ----------
        gid : str
            Group id
        feature : SeqFeature
            BioPython SeqFeature
        extra_tooltip : dict[str, str] | None, optional
            Extra tooltip dict
        """
        pass

    def __str__(self):
        seg_name = self.name
        seg_size = self.size
        seg_range = f"({self.start} - {self.end})"
        return f"{seg_name=}, {seg_size=}, {seg_range=}"

    def __repr__(self):
        return str(self)
