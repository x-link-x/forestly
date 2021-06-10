import repositories.area_repository as area_repository
import repositories.treetype_repository as treetype_repository
import repositories.tree_repository as tree_repository
import pdb

from models.area import Area
from models.treetype import TreeType
from models.tree import Tree

tree_repository.delete_all()
area_repository.delete_all()
treetype_repository.delete_all()

oak = TreeType("Oak")
elm = TreeType("Elm")
ash = TreeType("Ash")
birch = TreeType("Birch")
hazel = TreeType("Hazel")
rowan = TreeType("Rowan")
scots_pine = TreeType("Scots Pine")

treetype_repository.save(oak)
treetype_repository.save(elm)
treetype_repository.save(ash)
treetype_repository.save(birch)
treetype_repository.save(hazel)
treetype_repository.save(rowan)
treetype_repository.save(scots_pine)

area0000 = Area("00", "00")
area0100 = Area("01", "00")
area0200 = Area("02", "00")
area0001 = Area("00", "01")
area0101 = Area("01", "01")
area0201 = Area("02", "01")
area0002 = Area("00", "02")
area0102 = Area("01", "02")
area0202 = Area("02", "02")

area_repository.save(area0000)
area_repository.save(area0100)
area_repository.save(area0200)
area_repository.save(area0001)
area_repository.save(area0101)
area_repository.save(area0201)
area_repository.save(area0002)
area_repository.save(area0102)
area_repository.save(area0202)

tree1 = Tree(3, oak, area0102, 7, 4)
tree2 = Tree(10, ash, area0000, 2, 8)

tree_repository.save(tree1)
tree_repository.save(tree2)

tree_repository.select(2)

# print(area_repository.select(area0000.id).id)
# print(treetype_repository.select(oak.id).id)

# print(tree1.tree_type)
# print(tree2.area.get_grid_reference())

pdb.set_trace()