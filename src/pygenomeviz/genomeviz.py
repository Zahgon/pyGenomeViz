from __future__ import annotations

import io
from collections.abc import Mapping, Sequence
from copy import deepcopy
from pathlib import Path
from typing import Any, Callable

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.colorbar import Colorbar
from matplotlib.colors import LinearSegmentedColormap, Normalize, to_hex
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties
from matplotlib.gridspec import GridSpec
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar

from pygenomeviz.exception import (
    FeatureTrackNotFoundError,
    LinkRangeError,
    LinkTrackNotFoundError,
)
from pygenomeviz.track import FeatureSubTrack, FeatureTrack, LinkTrack, Track
from pygenomeviz.typing import Theme, TrackAlignType, Unit
from pygenomeviz.utils.helper import interpolate_color, size_label_formatter
from pygenomeviz.viewer import setup_viewer_html


class GenomeViz:
    """Genome Visualization Class"""

    # By default, after saving a figure using the `savefig()` method, figure object is
    # automatically deleted to avoid memory leaks (no display on jupyter notebook)
    # If you want to display the figure on jupyter notebook using `savefig()` method,
    # set clear_savefig=False.
    clear_savefig: bool = True

    def __init__(
        self,
        *,
        fig_width: float = 15,
        fig_track_height: float = 1.0,
        track_align_type: TrackAlignType = "left",
        feature_track_ratio: float = 0.25,
        link_track_ratio: float = 1.0,
        theme: Theme = "light",
        show_axis: bool = False,
    ):
        """
        Parameters
        ----------
        fig_width : float, optional
            Figure width
        fig_track_height : float, optional
            Figure height = `fig_track_height * track number`
        track_align_type : TrackAlignType, optional
            Figure track alignment type (`left`|`center`|`right`)
        feature_track_ratio : float, optional
            Feature track size ratio
        link_track_ratio : float, optional
            Link track size ratio
        theme : Theme, optional
            `light`: white background + black text, edge
            `dark`: black background + white text, edge
        show_axis : bool, optional
            Show axis for debug purpose
        """
        self._fig_width = fig_width
        self._fig_track_height = fig_track_height
        self._track_align_type: TrackAlignType = track_align_type
        self._feature_track_ratio = feature_track_ratio
        self._link_track_ratio = link_track_ratio
        self._show_axis = show_axis

        self._tracks: list[Track] = []
        self._plot_colorbar: Callable[[Figure], None] | None = None
        self._plot_scale_bar: Callable[[Axes], None] | None = None
        self._plot_axis_ticks: Callable[[Axes], None] | None = None

        self._mpl_style = {
            "light": "default",
            "dark": "dark_background",
        }[theme]

    ############################################################
    # Property
    ############################################################

    @property
    def figsize(self) -> tuple[float, float]:
        """Figure size (Width, Height)"""
        pass

    @property
    def feature_tracks(self) -> list[FeatureTrack]:
        """Feature tracks"""
        pass

    @property
    def link_tracks(self) -> list[LinkTrack]:
        """Link tracks"""
        pass

    ############################################################
    # Public Method
    ############################################################

    def get_tracks(self, *, subtrack: bool = True) -> list[Track]:
        """Get tracks

        Parameters
        ----------
        subtrack : bool, optional
            If True, include subtracks in FeatureTrack

        Returns
        -------
        tracks : list[Track]
            Tracks [`FeatureTrack`|`FeatureSubTrack`|`LinkTrack`]
        """
        pass

    def add_feature_track(
        self,
        name: str,
        segments: int
        | tuple[int, int]
        | Sequence[int | tuple[int, int]]
        | Mapping[str, int | tuple[int, int]],
        *,
        space: float | list[float] = 0.02,
        offset: int | TrackAlignType | None = None,
        labelsize: float = 20,
        labelmargin: float = 0.01,
        align_label: bool = True,
        label_kws: dict[str, Any] | None = None,
        line_kws: dict[str, Any] | None = None,
    ) -> FeatureTrack:
        """Add feature track

        Add feature track, and also add link track between feature tracks
        if other feature tracks already exist.

        Parameters
        ----------
        name : str
            Track name
        segments : int | tuple[int, int] | Sequence[int | tuple[int, int]] | Mapping[str, int | tuple[int, int]]
            Track segments definition. Segment sizes or ranges can be specified.
        space : float | list[float], optional
            Space ratio between segments.
            If `float`, all spaces are set to the same value.
            If `list[float]`, each space is set to the corresponding value
            (list size must be `len(segments) - 1`)
        offset : int | TrackAlignType | None, optional
            Offset int value or TrackAlignType (`left`|`center`|`right`)
            If None, offset is defined by GenomeViz `track_align_type` argument at initialization.
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

        Returns
        -------
        feature_track : FeatureTrack
            Feature track
        """  # noqa: E501
        pass

    def add_link(
        self,
        target1: tuple[str, int, int] | tuple[str, str | None, int, int],
        target2: tuple[str, int, int] | tuple[str, str | None, int, int],
        color: str = "grey",
        inverted_color: str | None = None,
        alpha: float = 0.8,
        v: float | None = None,
        vmin: float = 0,
        vmax: float = 100,
        size: float = 1.0,
        curve: bool = False,
        filter_length: int = 0,
        ignore_outside_range: bool = False,
        v_tooltip: float | None = None,
        **kwargs,
    ) -> None:
        """Add link patch to link track between adjacent feature tracks

        Parameters
        ----------
        target1 : tuple[str, int, int] | tuple[str, int | str | None, int, int]
            Target link1 `(track_name, start, end)` or `(track_name, target_segment, start, end)`
        target2 : tuple[str, int, int] | tuple[str, int | str | None, int, int]
            Target link2 `(track_name, start, end)` or `(track_name, target_segment, start, end)`
        color : str, optional
            Link color
        inverted_color : str | None, optional
            Inverted link color. If None, `color` is set.
        alpha : float, optional
            Color transparency
        v : float | None, optional
            Identity value for color interpolation. If None, no color interpolation is done.
        vmin : float, optional
            Min value for color interpolation
        vmax : float, optional
            Max value for color interpolation
        size : float, optional
            Link vertical size ratio for track
        curve : bool, optional
            If True, bezier curve link is plotted
        filter_length : int, optional
            If link length is shorter than `filter_length`, ignore it.
        ignore_outside_range : bool, optional
            If True and the link position is outside the range of the target track,
            ignore it without raising an error.
        v_tooltip: float | None, optional
            Identity value for only tooltip display.
            If no color interpolation is required, use this option instead of `v`.
        **kwargs: dict, optional
            Patch properties (e.g. `ec="black", lw=0.5, hatch="//", ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        """  # noqa: E501
        pass

    def set_scale_bar(
        self,
        *,
        ymargin: float = 1.0,
        labelsize: float = 15,
        scale_size_label: tuple[int, str] | None = None,
    ) -> None:
        """Set scale bar

        Parameters
        ----------
        ymargin : float, optional
            Scale bar y margin
        labelsize : float, optional
            Label size
        scale_size_label : tuple[int, str] | None, optional
            Scale bar size & label tuple (e.g. `(1000, "1.0 kb")`)
            If None, scale bar size & label are automatically set.
        """
        pass

    def set_scale_xticks(
        self,
        *,
        ymargin: float = 1.0,
        labelsize: float = 15,
        start: int = 0,
        unit: Unit | None = None,
    ) -> None:
        """Set scale xticks

        Parameters
        ----------
        ymargin : float, optional
            X ticks y margin
        labelsize : float, optional
            Label size
        start : int, optional
            X ticks start position
        unit : Unit | None, optional
            Display unit (`Gb`|`Mb`|`Kb`|`bp`)
        """
        pass

    def set_colorbar(
        self,
        colors: list[str] | None = None,
        *,
        alpha: float = 0.8,
        vmin: float = 0,
        vmax: float = 100,
        bar_height: float = 0.2,
        bar_width: float = 0.01,
        bar_left: float = 1.02,
        bar_bottom: float = 0,
        bar_label: str = "",
        bar_labelsize: float = 15,
        tick_labelsize: float = 10,
    ) -> None:
        """Set colorbar

        Parameters
        ----------
        colors : list[str] | None, optional
            Colors for bar
        alpha : float, optional
            Color transparency
        vmin : float, optional
            Colorbar min value
        vmax : float, optional
            Colorbar max value
        bar_height : float, optional
            Colorbar height ratio
        bar_width : float, optional
            Colorbar width ratio
        bar_left : float, optional
            Colorbar left position
        bar_bottom : float, optional
            Colorbar bottom position
        bar_label : str, optional
            Colorbar label
        bar_labelsize : float, optional
            Colorbar label size
        tick_labelsize : float, optional
            Colorbar tick label size
        """
        pass

    def plotfig(
        self,
        *,
        dpi: int = 100,
        fast_render: bool = True,
    ) -> Figure:
        """Plot figure

        Parameters
        ----------
        dpi : int, optional
            DPI
        fast_render : bool, optional
            Enable fast rendering mode using PatchCollection.
            Set fast_render=True by default, and set it to False
            when used in the `savefig_html()` method.
            Fast rendering mode cannot generate tooltips for html display.

        Returns
        -------
        fig : Figure
            Plot figure result
        """
        pass

    def savefig(
        self,
        savefile: str | Path,
        *,
        dpi: int = 100,
        pad_inches: float = 0.5,
    ) -> None:
        """Save figure to file

        Parameters
        ----------
        savefile : str | Path
            Save file
        dpi : int, optional
            DPI
        pad_inches : float, optional
            Padding inches

        Warnings
        --------
        To plot a figure that settings a user-defined legend, subtracks, or annotations,
        call `fig.savefig()` instead of `gv.savefig()`.
        """
        pass

    def savefig_html(
        self,
        html_outfile: str | Path | io.StringIO | io.BytesIO,
        figure: Figure | None = None,
    ) -> None:
        """Save figure in html format

        Parameters
        ----------
        html_outfile : str | Path | StringIO | BytesIO
            Output HTML file (*.html)
        figure : Figure | None, optional
            Save HTML viewer file using user customized figure.
            Set to output figure including user-specified legend, subtracks, etc.
            Target figure must be generated by `gv.plotfig(fast_render=False)`.
        """
        pass

    ############################################################
    # Private Method
    ############################################################

    def _update_track_status(self) -> None:
        """Update track status

        This method is called at the end of `add_feature_track()`
        """
        pass

    def _to_seg_name2range(
        self,
        segments: int
        | tuple[int, int]
        | Sequence[int | tuple[int, int]]
        | Mapping[str, int | tuple[int, int]],
    ) -> dict[str, tuple[int, int]]:
        """Convert segments type to `segment name` & `range` dict"""
        pass

    def _get_target_link_track(
        self,
        target1: tuple[str, str | None, int, int],
        target2: tuple[str, str | None, int, int],
    ) -> LinkTrack:
        pass

    def _get_gid2feature_dict(self) -> dict[str, dict[str, Any]]:
        """Get group ID & feature dict

        Returns
        -------
        gid2feature_dict : dict[str, dict[str, Any]]
            Group ID & feature dict
        """
        pass

    def _get_gid2link_dict(self) -> dict[str, dict[str, Any]]:
        """Get group ID & link dict

        Returns
        -------
        gid2link_dict : dict[str, dict[str, Any]]
            Group ID & link dict
        """
        pass

    def _setup_jupyter_inline(self) -> None:
        """Setup `%matplotline inline` magic command

        `plt.style.context()` overrides jupyter notebook
        default `%matplotlib inline` setting.
        Set `%matplotlib inline` on every plot to avoid this issue.

        [Bug]: mpl.style.context() stops plotting inline in Jupyter
        <https://github.com/matplotlib/matplotlib/issues/26716>
        """
        pass

    def __str__(self):
        ret_val = ""
        for feature_track in self.feature_tracks:
            ret_val += f"{feature_track}\n"
            for idx, seg in enumerate(feature_track.segments, 1):
                ret_val += f"  {idx}: {seg}\n"
        return ret_val
