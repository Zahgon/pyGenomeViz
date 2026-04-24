#!/usr/bin/env python
from __future__ import annotations

import argparse
import logging
import os
import shutil
from pathlib import Path

import pygenomeviz
from pygenomeviz.logger import init_logger
from pygenomeviz.scripts import CustomHelpFormatter, exit_handler, logging_timeit
from pygenomeviz.typing import GenbankDatasetName
from pygenomeviz.utils import load_example_genbank_dataset
from pygenomeviz.utils.download import GBK_DATASET

CLI_NAME = "pgv-download"


@exit_handler
@logging_timeit
def main():
    """Main function called from CLI"""
    pass


def get_args() -> argparse.Namespace:
    """Get arguments

    Returns
    -------
    args : argparse.Namespace
        Argument parameters
    """
    pass


if __name__ == "__main__":
    main()
