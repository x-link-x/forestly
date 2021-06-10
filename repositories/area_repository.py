from db.run_sql import run_sql
from models.area import Area

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

def delete(id):
    pass

def update(tree):
    pass

def trees():
    pass