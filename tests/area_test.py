import unittest
from forest.models.area import Area

class TestArea(unittest.TestCase):
    def setUp(self):
        self.area = Area("01", "02")

    def test_get_grid_reference_returns_0102(self):
        expected = "0102"
        actual = self.area.get_grid_reference()
        self.assertEqual(expected, actual)
        