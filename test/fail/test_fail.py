from unittest import TestCase


class FailTest(TestCase):
    """A test that fails."""
    def test_foo(self):
        self.assertTrue(False)
