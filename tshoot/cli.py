"""Script to run troubleshooter."""
from .troubleshooter import Troubleshooter


def _print_grey(text: str):
    """Print text in grey."""
    print(f"\033[90m{text}\033[0m")


def _read_line():
    """Read input from stdin."""
    return str(input()).strip()


def _read_multiline():
    """Read multiline input from stdin."""
    lines = []
    while True:
        line = str(input()).strip()
        if line == "":
            break
        else:
            lines.append(line)
    return "\n".join(lines)


def run():
    print("Running tshoot")
    troubleshooter = Troubleshooter()

    print("Problem: ")
    problem = _read_multiline()
    _print_grey(f"Problem: {problem}")

    output = troubleshooter.troubleshoot(problem=problem)
    print(f"Output: {output}")

    while True:
        print("Ask question: ")
        question = _read_line()
        _print_grey(f"Question: {question}")

        output = troubleshooter.ask(question=question)
        print(f"Output: {output}")
