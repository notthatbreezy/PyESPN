# Unit Tests for PyESPN #

from PyESPN import *
from login_data import *

import unittest

class TestPyESPN(unittest.TestCase):
    """Test basic functions in PyESPN class"""
    def setUp(self):
        self.search = PyESPN(API_KEY)

    def test_url(self):
        self.search.sports()
        self.assertEqual(self.search.status, "success")

    # def test_nba(self):
    #     self.nba_player('400')
    #     self.assertEqual(self.search.status, "success")

if __name__ == '__main__':
    unittest.main()