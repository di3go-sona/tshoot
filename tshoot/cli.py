"""Script to run troubleshooter."""
import subprocess
import argparse
import sys

from .troubleshooter import Troubleshooter
from .utils import _print_bold


def _read_input(args, eval_mode=False):
    """Read input from stdin."""
    if args.multiline:
        return _read_multiline()
    return _read_line()

def _read_line():
    """Read input from stdin."""
    line = str(input()).strip()
    if line.startswith("!"):
        command_line = line[1:]
        process = subprocess.run(command_line, shell=True, capture_output=True)
        process_output = process.stdout.decode("utf-8").strip()
        print(f"[📺][ Command output ] {process_output}")
        line += "\n" + process_output

    return line


        


def _read_multiline():
    """Read lines from stdin until EOF."""
    lines = []
    while True:
        try:
            line = _read_line()
            lines.append(line)
        except EOFError:
            break
        
    return "\n".join(lines)


def _parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Troubleshoot a problem with GPT-3.")
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="print debug information"
    )
    parser.add_argument(
        "--multiline", "-m",
        action="store_true",
        help="read multiple lines of input, terminate with CTRL-D"
    )

    return parser.parse_args()


def run():
    _print_bold("[🧨] Running tshoot")
    args = _parse_args()
    troubleshooter = Troubleshooter(**vars(args))

    while True:
        # print and flush to stdout to avoid buffering
        if args.multiline:
            print("[👨‍💻][ Multiline input, terminate with CTRL-D ]")
        else:
            print("[👨‍💻] ", end="")
        sys.stdout.flush()
        question = _read_input(args, eval_mode=True)

        print("[🤖] ", end="")
        sys.stdout.flush()
        output = troubleshooter.ask(question=question)
        for part in output:
            print(part, end="")
            sys.stdout.flush()
        print()
