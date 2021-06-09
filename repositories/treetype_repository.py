from db.run_sql import run_sql
from models.treetype import TreeType

def save(tree_type):
    sql = "INSERT INTO tree_types (name) VALUES (%s) RETURNING *"
    values = [tree_type.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    tree_type.id = id
    return tree_type

def select_all():
    pass


def delete_all():
    sql = "DELETE FROM tree_types"
    run_sql(sql)

def select(id):
    pass

def delete(id):
    pass

def update(tree):
    pass