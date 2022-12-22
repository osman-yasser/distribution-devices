# cli.py
"""
    this module used to parse the terminal parameters,
    using argparse library.
"""

import argparse

def read_user_cli_args():
    """Handle the CLI arguments and options."""
    parser = argparse.ArgumentParser(
        prog="get_perm",
        allow_abbrev=False,
        description="return pre-defined random permutations"
    )
    parser.add_argument(
        "-d",
        "--devices",
        type=int,
        required=True,
        metavar="DEVICES",
        help="number of devices",
    )
    parser.add_argument(
        "-t",
        "--test-cases",
        type=int,
        required=True,
        metavar="CASES",
        help="number of test cases",
    )
    parser.add_argument(
        "-l",
        "--meridians",
        type=int,
        required=True,
        metavar="LENGth",
        help="number of length lines"
    )
    parser.add_argument(
        "-w",
        "--latitudes",
        type=int,
        required=True,
        metavar="WIDTH",
        help="number of width lines"
    )
    return parser.parse_args()