"""
Various tools : parse_args
"""

import argparse


def parse_args():
    """
    Parses args

    Parameters: void
    Returns: args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose Output")
    parser.add_argument(
        "-f",
        "--file",
        dest="file",
        help="file",
    )

    return parser.parse_args()
