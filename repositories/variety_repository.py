from db.run_sql import run_sql
from models.variety import Variety
from models.tree import Tree
import repositories.area_repository as area_repository

def save(variety):
    sql = "INSERT INTO varieties (name) VALUES (%s) RETURNING *"
    values = [variety.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    variety.id = id
    return variety

def select_all():
    varieties = []
    sql = "SELECT * FROM varieties"
    results = run_sql(sql)
    for row in results:
        variety = Variety(row["name"], row["id"])
        varieties.append(variety)
    return varieties

def select(id):
    variety = None
    sql = "SELECT * FROM varieties WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        variety = Variety(result["name"], result["id"])
    return variety

def delete(id):
    sql = "DELETE FROM varieties WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM varieties"
    run_sql(sql)

def update(variety):
    sql = "UPDATE varieties SET (name) = ROW(%s) WHERE id = %s"
    values = [variety.name, variety.id]
    run_sql(sql, values)

def trees(variety):
    trees = []
    sql = "SELECT trees.* FROM trees WHERE trees.variety_id = %s"
    values = [variety.id]
    results = run_sql(sql, values)
    for row in results:
        area = area_repository.select(row["area_id"])
        tree = Tree(row["approx_age"], variety, area, row["x"], row["y"], row["id"])
        trees.append(tree)
    return trees