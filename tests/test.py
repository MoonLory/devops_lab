from unittest import TestCase
from handlers import pulls


class TestPrime(TestCase):
    def setUp(self):
        """Init"""

    def test_begin(self):
        self.assertNotEqual(len(pulls.get_pulls('open')), 0)
        self.assertNotEqual(len(pulls.get_pulls('closed')), 0)
        self.assertNotEqual(len(pulls.get_pulls('accepted')), 0)
        self.assertNotEqual(len(pulls.get_pulls('needs work')), 0)
        self.assertNotEqual(len(pulls.get_pulls('all')), 0)

    def tearDown(self):
        """Finish"""
