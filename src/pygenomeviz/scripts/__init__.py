from __future__ import annotations

import argparse
import logging
import os
import platform
import signal
import sys
import time
from functools import partial, wraps
from pathlib import Path
from typing import Callable, Type

import Bio
import matplotlib
from matplotlib.colors import is_color_like

import pygenomeviz
from pygenomeviz.align import AlignToolBase, Blast, MMseqs, MUMmer, ProgressiveMauve
from pygenomeviz.typing import AlnCliName

LOG_FILENAME = "pgv-cli.log"
ALIGN_COORDS_FILENAME = "align_coords.tsv"

CLI_NAME2TOOL: dict[AlnCliName, Type[AlignToolBase]] = {
    "pgv-blast": Blast,
    "pgv-mummer": MUMmer,
    "pgv-mmseqs": MMseqs,
    "pgv-pmauve": ProgressiveMauve,
}


class CustomHelpFormatter(argparse.RawTextHelpFormatter):
    def __init__(self, prog, indent_increment=2, max_help_position=40, width=None):
        super().__init__(prog, indent_increment, max_help_position, width)

    def _format_args(self, action, default_metavar):
        pass


def log_basic_env_info(
    cli_name: AlnCliName,
    log_params: dict | None,
) -> None:
    """Logging basic environment information

    Parameters
    ----------
    cli_name : str
        CLI name
    log_params : dict | None
        Log parameters
    """
    pass


def setup_argparser(
    parser: argparse.ArgumentParser,
    cli_name: AlnCliName,
) -> None:
    """Setup argument parser

    Parameters
    ----------
    parser : argparse.ArgumentParser
        Argument parser
    cli_name : CliNameList
        Setup target command line name
    """
    pass


def _setup_general_arg_group(general_arg_group: argparse._ArgumentGroup) -> None:
    """Setup general argument group for pgv-[blast|mummer|mmseqs|pmauve]

    Parameters
    ----------
    general_arg_group : argparse._ArgumentGroup
        General argument group
    """
    pass


def _setup_align_arg_group(
    align_arg_group: argparse._ArgumentGroup,
    cli_name: AlnCliName,
) -> None:
    """Setup alignment argument group for pgv-[blast|mummer|mmseqs]

    Parameters
    ----------
    align_arg_group : argparse._ArgumentGroup
        Alignment argument group
    cli_name : CliName
        Target command line name
    """
    pass


def _setup_fig_arg_group(
    fig_arg_group: argparse._ArgumentGroup,
    cli_name: AlnCliName,
) -> None:
    """Setup figure appearence argument group for pgv-[blast|mummer|mmseqs|pmauve]

    Parameters
    ----------
    fig_arg_group : argparse._ArgumentGroup
        Figure appearence argument group
    cli_name : CliName
        Target command line name
    """
    pass


def validate_args(args: argparse.Namespace, parser: argparse.ArgumentParser) -> None:
    """Validate command arguments

    Parameters
    ----------
    args : argparse.Namespace
        Command arguments
    parser : argparse.ArgumentParser
        Command parser
    """
    pass


def logging_timeit(
    func: Callable | None = None,
    /,
    *,
    show_func_name: bool = False,
    debug: bool = False,
):
    """Elapsed time logging decorator

    e.g. `Done (elapsed time: 82.3[s]) [module.function]`

    Parameters
    ----------
    func : Callable | None, optional
        Target function
    show_func_name : bool, optional
        If True, show elapsed time message with `module.function` definition
    debug : bool, optional
        If True, use `logger.debug` (By default `logger.info`)
    """
    pass


def exit_handler(func):
    """Exit handling decorator on exception

    The main purpose is logging on keyboard interrupt exception
    """
    pass
