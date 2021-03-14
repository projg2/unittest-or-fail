from unittest import TestCase, skipIf


class SkipAllTest(TestCase):
    """A test where all methods are skipped."""

    @skipIf(True, "skipping for testing's sake")
    def test_foo(self):
        pass
