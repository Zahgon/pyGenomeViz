from __future__ import annotations

import textwrap
from collections.abc import Sequence
from copy import deepcopy
from typing import TYPE_CHECKING, Any, Callable, Mapping, overload

import numpy as np
from Bio.SeqFeature import SeqFeature
from matplotlib.patches import Patch

from pygenomeviz.exception import SegmentNotFoundError, SubTrackNotFoundError
from pygenomeviz.patches import PLOTSTYLE2PATCH, Intron
from pygenomeviz.segment import FeatureSegment
from pygenomeviz.track import Track
from pygenomeviz.typing import HPos, PlotStyle, TrackAlignType, VPos
from pygenomeviz.utils.plot import plot_patches

if TYPE_CHECKING:
    from numpy.typing import NDArray


class FeatureTrack(Track):
    """Feature Track Class"""

    def __init__(
        self,
        name: str,
        seg_name2range: Mapping[str, tuple[int, int]],
        *,
        ratio: float = 1.0,
        space: float | list[float] = 0.01,
        offset: int | TrackAlignType = "left",
        labelsize: float = 20,
        labelmargin: float = 0.01,
        align_label: bool = True,
        label_kws: dict[str, Any] | None = None,
        line_kws: dict[str, Any] | None = None,
    ):
        """
        Parameters
        ----------
        name : str
            Track name
        seg_name2range : Mapping[str, tuple[int, int]]
            Segment name & range dict
        ratio : float, optional
            Track size ratio
        space : float | list[float], optional
            Space ratio between segments
        offset : int | TrackAlignType, optional
            Offset int value or TrackAlignType (`left`|`center`|`right`)
        labelsize : float, optional
            Track label size
        labelmargin : float, optional
            Track label margin
        align_label : bool, optional
            If True, align track label to the most left position.
            If False, set track label to first segment start position.
        label_kws : dict[str, Any] | None, optional
            Text properties (e.g. `dict(size=25, color="red", ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html>
        line_kws : dict[str, Any] | None, optional
            Axes.plot properties (e.g. `dict(color="grey", lw=0.5, ls="--", ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html>
        """
        label_kws = {} if label_kws is None else deepcopy(label_kws)
        line_kws = {} if line_kws is None else deepcopy(line_kws)
        line_kws.setdefault("color", "grey")
        line_kws.setdefault("lw", 1.0)

        super().__init__(name, ratio=ratio, zorder=1.0)

        segments: list[FeatureSegment] = []
        for seg_name, range in seg_name2range.items():
            segment = FeatureSegment(seg_name, *range, self)
            segments.append(segment)

        # Check space list length
        if isinstance(space, (list, tuple)):
            if len(space) != len(seg_name2range) - 1:
                raise ValueError(f"{len(space)=} is invalid!!")

        self._segments = segments
        self._space = space
        self._offset = offset
        self._labelsize = labelsize
        self._labelmargin = labelmargin
        self._align_label = align_label
        self._label_kws = label_kws
        self._line_kws = line_kws
        self._subtracks: list[FeatureSubTrack] = []

        self._label: str | None = None
        self._segment_sep_text_kws_list: Sequence[dict[str, Any] | None] = []

        self._max_track_total_seg_size: int | None = None

    ############################################################
    # Property
    ############################################################

    @property
    def label(self) -> str:
        """Track label (By default, `track.label` = `track.name`)"""
        pass

    @property
    def offset(self) -> int:
        """Track offset"""
        pass

    @property
    def segments(self) -> list[FeatureSegment]:
        """Segments"""
        pass

    @property
    def subtracks(self) -> list[FeatureSubTrack]:
        """Subtracks"""
        pass

    @property
    def total_seg_size(self) -> int:
        """Total segment size"""
        pass

    @property
    def spaces(self) -> list[int]:
        """Spaces between segments"""
        pass

    @property
    def max_track_total_seg_size(self) -> int:
        """Max track total segment size (Use space calculation)"""
        pass

    @property
    def plot_size(self) -> int:
        """Plot x size (`total_seg_size` + `sum(spaces)`)"""
        pass

    ############################################################
    # Public Method
    ############################################################

    def set_max_track_total_seg_size(self, max_track_total_seg_size: int) -> None:
        """Set max track total segment size

        This method is expected to be called within the GenomeViz instance
        to update track status. General users should not use this method.

        Parameters
        ----------
        max_track_total_seg_size : int
            Max track total segment size
        """
        pass

    def set_label(self, label: str) -> None:
        """Set track label (By default, `track.label` = `track.name`)

        Parameters
        ----------
        label : str
            Track label
        """
        pass

    def set_segment_sep(
        self,
        sep: bool | list[bool] = True,
        *,
        symbol: str = "//",
        size: float = 20,
        color: str = "grey",
        **kwargs,
    ) -> None:
        """Set segment separator symbol text

        Parameters
        ----------
        sep : bool | list[bool]
            If True, insert separator text between all segments.
            If list[bool], insert separator text between segments where True.
        symbol : str, optional
            Separator symbol text
        size : float, optional
            Separator symbol size
        color : str, optional
            Separator symbol color
        **kwargs : dict, optional
            Text properties
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html>
        """
        pass

    def add_subtrack(
        self,
        name: str | None = None,
        *,
        ratio: float = 1.0,
        ylim: tuple[int, int] = (0, 100),
    ) -> FeatureSubTrack:
        """Add subtrack for user-defined plot axes

        Parameters
        ----------
        name : str
            Track name
        ratio : float, optional
            Subtrack size ratio to feature track
        ylim : tuple[int, int], optional
            Axes ylim

        Returns
        -------
        subtrack : FeatureSubTrack
            Subtrack
        """
        pass

    def get_subtrack(self, name: str | None = None) -> FeatureSubTrack:
        """Get subtrack by name

        If no subtrack found, raise error.

        Parameters
        ----------
        name : str | None, optional
            Target subtrack name. If None, first subtrack is returned.

        Returns
        -------
        subtrack : FeatureSubTrack
            Target subtrack
        """
        pass

    def get_segment(
        self,
        name: str | None = None,
    ) -> FeatureSegment:
        """Get segment by name

        Parameters
        ----------
        name : str | None
            Target segment name. If None, first segment is returned.

        Returns
        -------
        segment : FeatureSegment
            Target segment
        """
        pass

    def add_text(
        self,
        x: float,
        text: str,
        *,
        target_seg: str | None = None,
        size: float = 15,
        vpos: VPos = "top",
        hpos: HPos = "left",
        ymargin: float = 0.2,
        rotation: float = 45,
        **kwargs,
    ) -> None:
        """Add text to track segment

        Parameters
        ----------
        x : float
            Text x coordinate
        text : str
            Text content
        target_seg : str | None, optional
            Target segment name. If None, first segment is selected.
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
            `segment.add_text()` method keyword arguments (e.g. `color="red", ...`)
        """
        pass

    def add_sublabel(
        self,
        text: str | None = None,
        *,
        target_seg: str | None = None,
        size: float = 12,
        pos: str = "bottom-left",
        ymargin: float = 0.2,
        rotation: float = 0,
        **kwargs,
    ) -> None:
        """Add sublabel to corners of the track segment

        Parameters
        ----------
        text : str | None, optional
            Text content
        target_seg : str | None, optional
            Target segment name. If None, first segment is selected.
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
        target_seg: str | None = None,
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
        target_seg : str | None, optional
            Target segment name. If None, first segment is selected.
        plotstyle : PlotStyle, optional
            Feature plot style (`bigarrow`|`arrow`|`bigbox`|`box`|`bigrbox`|`rbox`)
        arrow_shaft_ratio : float, optional
            Arrow shaft size ratio
        extra_tooltip : dict[str, str] | None, optional
            Extra tooltip dict for html figure
        label : str, optional
            Feature label
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
        target_seg: str | None = None,
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
        target_seg : str | None, optional
            Target segment name. If None, first segment is selected.
        plotstyle : PlotStyle, optional
            Feature plot style (`bigarrow`|`arrow`|`bigbox`|`box`|`bigrbox`|`rbox`)
        arrow_shaft_ratio : float, optional
            Arrow shaft size ratio
        label_type : str | None, optional
            Label type (e.g. `gene`,`protein_id`,`product`,etc...)
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
            (e.g. `dict(size=12, color="red", ...)`)
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
        target_seg: str | None = None,
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
        target_seg : str | None, optional
            Target segment name. If None, first segment is selected.
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
        target_seg: str | None = None,
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
        """Add exon features

        Parameters
        ----------
        features : SeqFeature | list[SeqFeature]
            BioPython SeqFeature or SeqFeature list
        target_seg : str | None, optional
            Target segment name. If None, first segment is selected.
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

    @overload
    def transform_coord(self, x: int, *, target_seg: str | None = None) -> int: ...
    @overload
    def transform_coord(self, x: float, *, target_seg: str | None = None) -> float: ...
    @overload
    def transform_coord(
        self, x: NDArray, *, target_seg: str | None = None
    ) -> NDArray[np.float64]: ...

    def transform_coord(
        self,
        x: int | float | NDArray,
        *,
        target_seg: str | None = None,
    ) -> int | float | NDArray[np.float64]:
        """Transform segment-level coordinate to track-level coordinate

        Parameters
        ----------
        x : int | float | NDArray
            Segment-level coordinate(s)
        target_seg : str | None, optional
            Target segment name. If None, first segment is selected.

        Returns
        -------
        transform_x : int | float| NDArray[np.float64]
            Track-level coordinate(s)
        """
        pass

    def plot_all(self, fast_render: bool = True) -> None:
        """Plot all objects (Expected to be called in `gv.plotfig()`)

        1. Plot track label
        2. Plot segment lines
        3. Plot segment separator
        4. Plot features
        5. Plot texts

        Parameters
        ----------
        fast_render : bool, optional
            Enable fast rendering using PatchCollection plot style.
        """
        pass

    ############################################################
    # Private Method
    ############################################################

    def _plot_track_label(self) -> None:
        """Plot track label"""
        pass

    def _plot_segment_lines(self) -> None:
        """Plot lines for each segment"""
        pass

    def _plot_segment_sep(self) -> None:
        """Plot break symbol for each segment"""
        pass

    def _plot_features(
        self,
        fast_render: bool = True,
    ) -> None:
        """Plot features for each segment

        Parameters
        ----------
        fast_render : bool, optional
            Enable fast rendering using PatchCollection plot style.
        """
        pass

    def _plot_exon_features(
        self,
        fast_render: bool = True,
    ) -> None:
        """Plot exon features for each segment

        Parameters
        ----------
        fast_render : bool, optional
            Enable fast rendering using PatchCollection plot style.
        """
        pass

    def _plot_texts(self) -> None:
        """Plot texts"""
        pass

    def _extract_exon_intron_locs(
        self,
        feature: SeqFeature,
    ) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        """Extract exon & intron locations

        Parameters
        ----------
        feature : SeqFeature
            Exon Feature

        Returns
        -------
        exon_locs : list[tuple[int, int]]
            Exon locations
        intron_locs : list[tuple[int, int]]
            Intron locations
        """
        pass

    def __str__(self):
        track_segments = {seg.name: (seg.start, seg.end) for seg in self.segments}
        return textwrap.dedent(
            f"""
            track_name='{self.name}' ({len(self.segments)} segments)
            {track_segments=}
            """
        )[1:-1]

    def __repr__(self):
        return str(self)


class FeatureSubTrack(Track):
    """Feature SubTrack Class"""

    def __init__(
        self,
        name: str,
        *,
        ratio: float,
        feature_track: FeatureTrack,
    ):
        """
        Parameters
        ----------
        name : str
            Track name
        ratio : float, optional
            Track size ratio
        feature_track : FeatureTrack
            Parent feature track to which subtrack belongs
        """
        super().__init__(name, ratio=ratio)
        self._feature_track = feature_track
        self.transform_coord = self.feature_track.transform_coord

    @property
    def feature_track(self) -> FeatureTrack:
        """Parent feature track to which subtrack belongs"""
        pass

    def set_ylim(self, ylim: tuple[float, float]) -> None:
        """Set track ylim"""
        pass
