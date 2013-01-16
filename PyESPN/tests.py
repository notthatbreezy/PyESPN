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
        self.assertTrue(len(self.search.sport_list.items()) > 1)

if __name__ == '__main__':
    unittest.main()