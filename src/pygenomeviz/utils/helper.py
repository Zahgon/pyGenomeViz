from __future__ import annotations

from typing import overload

import matplotlib.pyplot as plt
import numpy as np
from Bio.SeqFeature import SeqFeature
from matplotlib.colors import LinearSegmentedColormap, Normalize, to_hex

from pygenomeviz.typing import Unit


class ColorCycler:
    """Color Cycler Class"""

    counter = 0
    cmap = plt.get_cmap("tab10")  # type: ignore

    def __new__(cls, n: int | None = None) -> str:
        """Get hexcolor cyclically from cmap by counter or user specified number

        `ColorCycler()` works same as `ColorCycler.get_color()` (syntactic sugar)

        Parameters
        ----------
        n : int | None, optional
            Number for color cycle. If None, counter class variable is used.

        Returns
        -------
        hexcolor : str
            Cyclic hexcolor string
        """
        return cls.get_color(n)

    @classmethod
    def reset_cycle(cls) -> None:
        """Reset cycle counter"""
        pass

    @classmethod
    def set_cmap(cls, name: str) -> None:
        """Set colormap (Default: `tab10`)"""
        pass

    @classmethod
    def get_color(cls, n: int | None = None) -> str:
        """Get hexcolor cyclically from cmap by counter or user specified number

        Parameters
        ----------
        n : int | None, optional
            Number for color cycle. If None, counter class variable is used.

        Returns
        -------
        hexcolor : str
            Cyclic hexcolor string
        """
        pass

    @classmethod
    def get_color_list(cls, n: int | None = None) -> list[str]:
        """Get hexcolor list of colormap

        Parameters
        ----------
        n : int | None, optional
            If n is None, all(=cmap.N) hexcolors are extracted from colormap.
            If n is specified, hexcolors are extracted from n equally divided colormap.

        Returns
        -------
        hexcolor_list : list[str]
            Hexcolor list
        """
        pass


def is_pseudo_feature(feature: SeqFeature) -> bool:
    """Check target feature is pseudo or not from qualifiers tag

    Parameters
    ----------
    feature : SeqFeature
        Target feature

    Returns
    -------
    check_result : bool
        pseudo check result
    """
    pass


def extract_features_within_range(
    features: list[SeqFeature],
    *,
    target_range: tuple[int, int],
) -> list[SeqFeature]:
    """Extract features by target range

    Parameters
    ----------
    features : list[SeqFeature]
        Features to be extracted
    target_range : tuple[int, int]
        Target range

    Returns
    -------
    range_features : list[SeqFeature]
        Features within target range
    """
    pass


def to_stack_features(features: list[SeqFeature]) -> list[list[SeqFeature]]:
    """Convert feature list to non-overlap stack feature list of lists

    Parameters
    ----------
    features : list[SeqFeature]
        Features

    Returns
    -------
    stack_features : list[list[SeqFeature]]
        Stacked features
    """
    pass


def interpolate_color(
    base_color: str,
    v: float,
    vmin: float = 0,
    vmax: float = 100,
) -> str:
    """Interpolate the base color between vmin and vmax

    `vmin[nearly white] <= v <= vmax[base_color]`

    Parameters
    ----------
    base_color : str
        Base color for interpolation
    v : float
        Interpolation value
    vmin : float, optional
        Min value
    vmax : float, optional
        Max value

    Returns
    -------
    interpolate_color : str
        Interpolated hexcolor
    """
    pass


@overload
def size_label_formatter(size: float, unit: Unit | None = None) -> str: ...
@overload
def size_label_formatter(size: list[float], unit: Unit | None = None) -> list[str]: ...
def size_label_formatter(
    size: float | list[float], unit: Unit | None = None
) -> str | list[str]:
    """Format scale size to human readable style (e.g. 1000 -> `1.0 Kb`))

    Parameters
    ----------
    size : float | list[float]
        Scale size (or size list)
    unit : Unit | None, optional
        Format target unit (`Gb`|`Mb`|`Kb`|`bp`)

    Returns
    -------
    format_size : str | list[str]
        Formatted size (or size list)
    """
    pass
