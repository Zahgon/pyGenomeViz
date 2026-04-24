from __future__ import annotations

from matplotlib.axes import Axes


class Track:
    """Track Base Class"""

    def __init__(
        self,
        name: str,
        *,
        ratio: float = 1.0,
        zorder: float = 0.0,
    ):
        self._name = name
        self._ratio = ratio
        self._zorder = zorder
        self._xlim: tuple[int, int] | None = None
        self._ylim: tuple[float, float] = (-1.0, 1.0)
        self._ax: Axes | None = None

    ############################################################
    # Property
    ############################################################

    @property
    def name(self) -> str:
        """Track name"""
        pass

    @property
    def ratio(self) -> float:
        """Track size ratio"""
        pass

    @property
    def zorder(self) -> float:
        """Track zorder"""
        pass

    @property
    def xlim(self) -> tuple[int, int]:
        """Track axes x min-max tuple"""
        pass

    @property
    def ylim(self) -> tuple[float, float]:
        """Track axes y min-max tuple"""
        pass

    @property
    def ax(self) -> Axes:
        """Track axes

        Can't access ax property before calling GenomeViz class `plotfig` method.

        Returns
        -------
        ax : Axes
            Matplotlib axes
        """
        pass

    ############################################################
    # Public Method
    ############################################################

    def set_ratio(self, ratio: float) -> None:
        """Set track size ratio"""
        pass

    def set_xlim(self, xlim: tuple[int, int]) -> None:
        """Set track xlim"""
        pass

    def set_ax(self, ax: Axes, show_axis: bool = False) -> None:
        """Set track axes

        Parameters
        ----------
        ax : Axes
            Matplotlib axes
        show_axis : bool, optional
            Show axis for debug purpose
        """
        pass

    ############################################################
    # Private Method
    ############################################################

    def _initalize_axes(self, ax: Axes, show_axis: bool = False) -> None:
        """Initialize axes properties

        Parameters
        ----------
        ax : Axes
            Matplotlib axes
        show_axis : bool, optional
            Show axis for debug purpose
        """
        pass
