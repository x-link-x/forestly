from db.run_sql import run_sql
from models.tree import Tree
import repositories.treetype_repository as treetype_repository
import repositories.area_repository as area_repository

def save(tree):
    sql = "INSERT INTO trees (approx_age, tree_type_id, area_id, x, y) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [tree.approx_age, tree.tree_type.id, tree.area.id, tree.x, tree.y]
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
    tree = None
    sql = "SELECT * FROM trees WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        tree_type = treetype_repository.select(result["tree_type"])
        area = area_repository.select(result["area"])
        tree = Tree(result["approx_age"], tree_type, area, result["x"], result["y"], result["id"])
    return tree
   

def delete(id):
    pass

def update(tree):
    