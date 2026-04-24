from __future__ import annotations

import uuid
from copy import deepcopy
from dataclasses import dataclass
from typing import Any

from matplotlib.patches import Patch

from pygenomeviz.exception import LinkRangeError
from pygenomeviz.patches import Link
from pygenomeviz.segment import FeatureSegment
from pygenomeviz.track import FeatureTrack, Track
from pygenomeviz.utils.plot import plot_patches


class LinkTrack(Track):
    """Link Track Class"""

    def __init__(
        self,
        name: str,
        *,
        ratio: float = 1.0,
        upper_feature_track: FeatureTrack,
        lower_feature_track: FeatureTrack,
    ):
        """
        Parameters
        ----------
        name : str
            Track name
        upper_feature_track : FeatureTrack
            Upper feature track
        lower_feature_track : FeatureTrack
            Lower feature track
        ratio : float, optional
            Track size ratio
        """
        super().__init__(name, ratio=ratio, zorder=0.0)

        self._upper_feature_track = upper_feature_track
        self._lower_feature_track = lower_feature_track

        self._link_record_list: list[LinkRecord] = []
        self._gid2link_dict: dict[str, dict[str, Any]] = {}

    @property
    def upper_feature_track(self) -> FeatureTrack:
        """Upper feature track"""
        pass

    @property
    def lower_feature_track(self) -> FeatureTrack:
        """Lower feature track"""
        pass

    @property
    def link_record_list(self) -> list[LinkRecord]:
        """Link record list"""
        pass

    @property
    def gid2link_dict(self) -> dict[str, dict[str, Any]]:
        """gid & link dict"""
        pass

    def add_link(
        self,
        upper_seg: FeatureSegment,
        upper_start: int,
        upper_end: int,
        lower_seg: FeatureSegment,
        lower_start: int,
        lower_end: int,
        *,
        v: float | None = None,
        size: float = 1.0,
        curve: bool = False,
        **kwargs,
    ) -> None:
        """Add link

        Parameters
        ----------
        upper_seg : FeatureSegment
            Upper segment
        upper_start : int
            Upper segment link start position
        upper_end : int
            Upper segment link end postion
        lower_seg : FeatureSegment
            Lower segment
        lower_start : int
            Lower segment link start position
        lower_end : int
            Lower segment link end postion
        v : float | None, optional
            Identity value for color interpolation
        size : float, optional
            Link vertical size ratio for track
        curve : bool, optional
            Curve or not
        **kwargs: dict, optional
            Patch properties (e.g. `ec="black", lw=0.5, hatch="//", ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        """
        pass

    def plot_links(self, fast_render: bool = True) -> None:
        """Plot links

        Parameters
        ----------
        fast_render : bool, optional
            Enable fast rendering using PatchCollection plot style.
        """
        pass


@dataclass
class LinkRecord:
    track1: FeatureTrack
    seg1: FeatureSegment
    start1: int
    end1: int
    track2: FeatureTrack
    seg2: FeatureSegment
    start2: int
    end2: int
    v: float | None = None
    ylim: tuple[float, float] = (-1, 1)
    curve: bool = False
    patch_kws: dict[str, Any] | None = None

    def __post_init__(self):
        # Generate uuid for patch group id
        self._gid = f"Link-{uuid.uuid4().hex}"

    @property
    def gid(self) -> str:
        """Group ID"""
        pass

    @property
    def length1(self) -> int:
        """Length1"""
        pass

    @property
    def length2(self) -> int:
        """Length2"""
        pass

    def to_patch(self) -> Link:
        """Convert to link patch

        Returns
        -------
        link_patch : Link
            Link patch
        """
        pass

    def to_dict(self) -> dict[str, Any]:
        """Convert to dict for tooltip display

        Returns
        -------
        link_dict : dict[str, Any]
            link dict
        """
        pass
