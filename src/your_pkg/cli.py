import argparse
from typing import Sequence
from .your_module import check_string_in_file


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog='check_string_in_file')
    parser.add_argument(
        'filenames',
        nargs='*',
        help='Filenames to process.',
    )
 
    args = parser.parse_args(argv)
    results = [
        check_string_in_file(filename)
        for filename in args.filenames
    ]
    return int(any(results))


