from __future__ import annotations

from collections import defaultdict

from matplotlib.axes import Axes
from matplotlib.collections import PatchCollection
from matplotlib.patches import Patch


def plot_patches(
    patches: list[Patch],
    ax: Axes,
    fast_render: bool = True,
) -> None:
    """Plot patches

    Parameters
    ----------
    patches : list[Patch]
        Patches
    ax : Axes
        Axes
    fast_render: bool, optional
        Enable fast rendering using PatchCollection plot style.
    """
    pass
