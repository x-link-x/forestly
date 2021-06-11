from db.run_sql import run_sql
from models.variety import Variety

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


def delete_all():
    sql = "DELETE FROM varieties"
    run_sql(sql)

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

def update(variety):
    pass

def locations():
    pass