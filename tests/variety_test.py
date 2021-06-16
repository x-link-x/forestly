import unittest
from models.variety import Variety

class TestVariety(unittest.TestCase):
    def setUp(self):
        self.variety = Variety("Oak")

    def test_variety_has_name(self):
        expected = "Oak"
        actual = self.variety.name
        self.assertEqual(expected, actual)


