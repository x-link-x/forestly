from db.run_sql import run_sql
from models.area import Area
from models.tree import Tree
import repositories.variety_repository as variety_repository

def save(area):
    sql = "INSERT INTO areas (easting, northing) VALUES (%s, %s) RETURNING *"
    values = [area.easting, area.northing]
    results = run_sql(sql, values)
    id = results[0]['id']
    area.id = id
    return area

def select_all():
    areas = []
    sql = "SELECT * FROM areas"
    results = run_sql(sql)
    for row in results:
        area = Area(row["easting"], row["northing"], row["id"])
        areas.append(area)
    return areas

def delete_all():
    sql = "DELETE FROM areas"
    run_sql(sql)

def select(id):
    area = None
    sql = "SELECT * FROM areas WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        area = Area(result["easting"], result["northing"], result["id"])
    return area
    
def update(area):
    sql = "UPDATE areas SET (easting, northing) = (%s, %s) WHERE id = %s"
    values = [area.easting, area.northing, area.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM areas WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def trees(area):
    trees = []
    sql = "SELECT trees.* FROM trees WHERE trees.area_id = %s"
    values = [area.id]
    results = run_sql(sql, values)
    for row in results:
        variety = variety_repository.select(row["variety_id"])
        tree = Tree(row["approx_age"], variety, area, row["x"], row["y"], row["notes"], row["id"])
        trees.append(tree)
        trees.sort(key=lambda tree: tree.variety.name)
    return trees
