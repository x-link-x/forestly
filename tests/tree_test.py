import unittest
from models.tree import Tree

class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree(10, "Oak", "0102", 7, 4)

    def test_tree_has_age(self):
        expected = 10
        actual = self.tree.approx_age
        self.assertEqual(expected, actual)

    def test_tree_has_type(self):
        expected = "Oak"
        actual = self.tree.tree_type
        self.assertEqual(expected, actual)

    def test_tree_get_location_method_returns_017024(self):
        expected = "017024"
        actual = self.tree.get_location()
        self.assertEqual(expected, actual)

        







