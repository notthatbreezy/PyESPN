# Unit Tests for PyESPN #

from PyESPN import *
from login_data import *

import unittest

class TestPyESPN(unittest.TestCase):
    """Test basic functions in PyESPN class"""
    def setUp():
        self.search = PyESPN(main_url, API_KEY)

    def test_url(self):

