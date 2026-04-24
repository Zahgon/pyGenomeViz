from __future__ import annotations

import logging
import sys
from pathlib import Path


def init_null_logger():
    """Initialize package root logger with NullHandler

    Configuring package root null logger for a library
    https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library
    """
    pkg_root_name = __name__.split(".")[0]
    logger = logging.getLogger(pkg_root_name)
    logger.addHandler(logging.NullHandler())


def init_logger(
    *,
    quiet: bool = False,
    verbose: bool = False,
    log_file: str | Path | None = None,
):
    """Initialize package root logger with StreamHandler(& FileHandler)

    Configuring package root default logger for a CLI tool

    Parameters
    ----------
    quiet : bool, optional
        If True, no print info log on screen
    verbose: bool, optional
        If True & quiet=False, print debug log on screen
    log_file : str | Path | None, optional
        Log file
    """
    pass
