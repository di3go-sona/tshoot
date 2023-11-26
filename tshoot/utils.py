def _grey(text: str):
    """Return text in grey."""
    return f"\033[90m{text}\033[0m"


def _bold(text: str):
    """Return text in bold."""
    return f"\033[1m{text}\033[0m"


def _print_grey(text: str):
    """Print text in grey."""
    print(_grey(text))


def _print_bold(text: str):
    """Print text in bold."""
    print(_bold(text))
