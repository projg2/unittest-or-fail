from unittest import TestCase, SkipTest


class SkipSetUpClass(TestCase):
    """A test case that is skipped inside setUpClass()."""

    @classmethod
    def setUpClass(cls):
        raise SkipTest("skip in setUpClass()")

    def test_foo(self):
        pass
