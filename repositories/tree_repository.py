from db.run_sql import run_sql
from models.tree import Tree
import repositories.treetype_repository as treetype_repository
import repositories.area_repository as area_repository

def save(tree):
    sql = "INSERT INTO trees (approx_age, tree_type_id, x, y, area_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [tree.approx_age, tree.tree_type.id, tree.x, tree.y, tree.area.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    tree.id = id
    return tree

def select_all():
    trees = []
    sql = "SELECT * FROM trees"
    results = run_sql(sql)
    for row in results:
        tree_type = treetype_repository.select(row['tree_type_id'])
        area = area_repository.select(row['area_id'])
        grid_reference = area.get_grid_reference()
        tree = Tree(row["approx_age"], tree_type.name, grid_reference, row["x"], row["y"], row["id"])
        trees.append(tree)
    return trees


def delete_all():
    sql = "DELETE FROM trees"
    run_sql(sql)

def select(id):
    pass

def delete(id):
    pass

def update(tree):
    pass