#!/usr/bin/env python
from __future__ import annotations

import argparse
import importlib.util
import os
import shlex
import subprocess as sp
import textwrap
from pathlib import Path

import pygenomeviz
from pygenomeviz.scripts import exit_handler

CLI_NAME = "pgv-gui"


@exit_handler
def main() -> None:
    """Launch pyGenomeViz WebApp"""
    pass


def get_args(cli_args: list[str] | None = None) -> argparse.Namespace:
    """Get arguments

    Parameters
    ----------
    cli_args : list[str] | None, optional
        CLI arguments (Used in unittest)

    Returns
    -------
    args : argparse.Namespace
        Argument parameters
    """
    pass
