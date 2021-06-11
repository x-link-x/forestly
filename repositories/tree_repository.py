from db.run_sql import run_sql
from models.tree import Tree
import repositories.variety_repository as variety_repository
import repositories.area_repository as area_repository

def save(tree):
    sql = "INSERT INTO trees (approx_age, variety_id, area_id, x, y) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [tree.approx_age, tree.variety.id, tree.area.id, tree.x, tree.y]
    results = run_sql(sql, values)
    id = results[0]['id']
    tree.id = id
    return tree

def select_all():
    trees = []
    sql = "SELECT * FROM trees"
    results = run_sql(sql)
    for row in results:
        variety = variety_repository.select(row['variety_id'])
        area = area_repository.select(row['area_id'])
        grid_reference = area.get_grid_reference()
        tree = Tree(row["approx_age"], variety.name, grid_reference, row["x"], row["y"], row["id"])
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
        variety = variety_repository.select(result["variety_id"])
        area = area_repository.select(result["area_id"])
        tree = Tree(result["approx_age"], variety, area, result["x"], result["y"], result["id"])
    return tree

def delete(id):
    sql = "DELETE FROM trees WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(tree):
    sql = "UPDATE trees SET (approx_age, variety_id, area_id, x, y) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [tree.approx_age, tree.variety, tree.area, tree.x, tree.y, tree.id]
    run_sql(sql, values)