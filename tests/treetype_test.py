import unittest
from forest.models.treetype import TreeType

class TestTreeType(unittest.TestCase):
    def setUp(self):
        self.tree_type = TreeType("Oak")

    def test_tree_type_has_name(self):
        expected = "Oak"
        actual = self.tree_type.name
        self.assertEqual(expected, actual)

    # def test_tree_type_get_locations_returns_a_list(self):
    #     expected = []
    #     actual = self.tree_type.get_locations()
    #     self.assertEqual(expected, actual)

