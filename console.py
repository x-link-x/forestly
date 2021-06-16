import repositories.area_repository as area_repository
import repositories.variety_repository as variety_repository
import repositories.tree_repository as tree_repository
import pdb

from models.area import Area
from models.variety import Variety
from models.tree import Tree

tree_repository.delete_all()
area_repository.delete_all()
variety_repository.delete_all()

oak = Variety("Oak")
elm = Variety("Elm")
ash = Variety("Ash")
birch = Variety("Birch")
hazel = Variety("Hazel")
rowan = Variety("Rowan")
scots_pine = Variety("Scots Pine")

variety_repository.save(oak)
variety_repository.save(elm)
variety_repository.save(ash)
variety_repository.save(birch)
variety_repository.save(hazel)
variety_repository.save(rowan)
variety_repository.save(scots_pine)

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

tree1 = Tree(3, oak, area0102, 7, 4, "new sapling")
tree2 = Tree(10, ash, area0000, 2, 8, "established tree")
tree3 = Tree(100, elm, area0200, 4, 5, "established tree")
tree4 = Tree(140, hazel, area0200, 7, 1, "struck by lightning last year")
tree5 = Tree(80, rowan, area0000, 1, 4, "established tree")
tree6 = Tree(1, scots_pine, area0101, 6, 3, "new sapling")
tree7 = Tree(1, scots_pine, area0101, 8, 1, "new sapling")

tree_repository.save(tree1)
tree_repository.save(tree2)
tree_repository.save(tree3)
tree_repository.save(tree4)
tree_repository.save(tree5)
tree_repository.save(tree6)
tree_repository.save(tree7)

pdb.set_trace()
