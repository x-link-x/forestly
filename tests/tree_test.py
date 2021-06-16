import unittest
from models.tree import Tree

class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree(10, "Oak", "0102", 7, 4, "new sapling")

    def test_tree_has_age(self):
        expected = 10
        actual = self.tree.approx_age
        self.assertEqual(expected, actual)

    def test_tree_has_variety(self):
        expected = "Oak"
        actual = self.tree.variety
        self.assertEqual(expected, actual)



        







