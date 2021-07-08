import unittest
from models.variety import Variety

class TestVariety(unittest.TestCase):
    def setUp(self):
        self.variety = Variety("Oak")

    def test_variety_has_name(self):
        expected = "Oak"
        actual = self.variety.name
        self.assertEqual(expected, actual)

    # def test_variety_get_locations_returns_a_list(self):
    #     expected = []
    #     actual = self.variety.get_locations()
    #     self.assertEqual(expected, actual)

