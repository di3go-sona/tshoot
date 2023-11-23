def _print_grey(text: str):
    """Print text in grey."""
    print(f"\033[90m{text}\033[0m")


def _print_bold(text: str):
    """Print text in bold."""
    print(f"\033[1m{text}\033[0m")
