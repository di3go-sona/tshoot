import unittest
from tshoot.utils import _grey, _bold, _print_grey, _print_bold

class TestUtils(unittest.TestCase):
    def test_grey(self):
        result = _grey("Hello")
        self.assertEqual(result, "\033[90mHello\033[0m")

    def test_bold(self):
        result = _bold("World")
        self.assertEqual(result, "\033[1mWorld\033[0m")

    def test_print_grey(self):
        # Redirect stdout to capture printed output
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        _print_grey("Print in grey")
        sys.stdout = sys.__stdout__  # Restore stdout

        self.assertEqual(captured_output.getvalue().strip(), "\033[90mPrint in grey\033[0m")

    def test_print_bold(self):
        # Redirect stdout to capture printed output
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        _print_bold("Print in bold")
        sys.stdout = sys.__stdout__  # Restore stdout

        self.assertEqual(captured_output.getvalue().strip(), "\033[1mPrint in bold\033[0m")

if __name__ == '__main__':
    unittest.main()