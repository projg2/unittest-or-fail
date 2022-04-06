#!/usr/bin/env python
"""Run unittests or fail if no tests are found"""

import sys
from unittest import main, TextTestRunner

__version__ = "2"


class NonZeroTextTestRunner(TextTestRunner):
    """
    TextTestRunner modified to fail when no tests are found.
    """

    def run(self, test):
        result = super().run(test)
        if result.testsRun == 0 and not result.skipped:
            self.stream.writeln("No tests found -- failing")
            sys.exit(3)
        return result


if __name__ == "__main__":
    main(module=None, testRunner=NonZeroTextTestRunner)
