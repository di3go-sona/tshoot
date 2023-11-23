"""Script to run troubleshooter."""
import argparse
import sys

from .troubleshooter import Troubleshooter
from .utils import _print_bold


def _read_line():
    """Read input from stdin."""
    return str(input()).strip()


def _read_multiline():
    """Read lines from stdin until EOF."""
    lines = []
    while True:
        line = _read_line()
        if not line:
            break
        lines.append(line)
    return "\n".join(lines)


def _parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Troubleshoot a problem with GPT-3.")
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="print debug information"
    )
    return parser.parse_args()


def run():
    _print_bold("[🧨] Running tshoot")
    args = _parse_args()
    troubleshooter = Troubleshooter(**vars(args))

    while True:
        # print and flush to stdout to avoid buffering
        print("[👨‍💻]", end="")
        sys.stdout.flush()
        question = _read_line()

        print("[🤖]", end="")
        sys.stdout.flush()
        output = troubleshooter.ask(question=question)
        for part in output:
            print(part, end="")
            sys.stdout.flush()
        print()
