import repositories.tree_repository as tree_repository
from models.tree import Tree
from models.treetype import TreeType


oak = TreeType("Oak")

tree1 = Tree(3, oak, "0102", 7, 4)
tree_repository.save(tree1)

print(tree1.tree_type)