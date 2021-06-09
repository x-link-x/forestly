import repositories.tree_repository as tree_repository
from models.tree import Tree

tree1 = Tree(3, "Oak", "0102", 7, 4)
tree_repository.save(tree1)