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

tree1 = Tree(3, oak, area0102, 7, 4)
tree2 = Tree(10, ash, area0000, 2, 8)

tree_repository.save(tree1)
tree_repository.save(tree2)

tree_repository.select(tree1.id)
area_repository.select(area0101.id)
variety_repository.select(oak.id)

# print(area_repository.select(area0000.id).id)
# print(variety_repository.select(oak.id).id)


# print(tree2.area.get_grid_reference())

pdb.set_trace()