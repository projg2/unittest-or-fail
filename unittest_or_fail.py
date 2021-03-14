#!/usr/bin/env python

import sys
from unittest import main, TextTestRunner


class NonZeroTextTestRunner(TextTestRunner):
    """
    TextTestRunner modified to fail when no tests are found.
    """

    def run(self, test):
        result = super().run(test)
        if result.testsRun == 0:
            self.stream.writeln("No tests found -- failing")
            sys.exit(3)
        return result


if __name__ == "__main__":
    main(module=None, testRunner=NonZeroTextTestRunner)
