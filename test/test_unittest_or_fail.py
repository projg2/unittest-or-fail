import os.path
import subprocess
import sys

from unittest import TestCase, expectedFailure


TEST_DIR = os.path.dirname(__file__)


class UnittestOrFailTest(TestCase):
    def assertResult(self, subdir, expected):
        p = subprocess.Popen(
            [sys.executable, '-m', 'unittest_or_fail', 'discover',
             '-s', os.path.join(TEST_DIR, subdir)],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        sout, serr = p.communicate()
        sout = "".join(f"\nsout: {x}" for x in sout.decode().splitlines())
        serr = "".join(f"\nserr: {x}" for x in serr.decode().splitlines())
        self.assertEqual(p.wait(), expected,
                         f"Unexpected unittest_or_fail.py result: "
                         f"{p.returncode}, expected: {expected}"
                         f"{sout}{serr}")

    def test_good(self):
        self.assertResult('good', 0)

    def test_fail(self):
        self.assertResult('fail', 1)

    def test_skip_all(self):
        self.assertResult('skip-all', 0)

    @expectedFailure
    def test_skip_setUpClass(self):
        self.assertResult('skip-setupclass', 0)

    def test_no_files(self):
        self.assertResult('no-files', 3)

    def test_no_methods(self):
        self.assertResult('no-methods', 3)
