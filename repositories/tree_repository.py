from db.run_sql import run_sql
from models.tree import Tree

def save(tree):
    sql = "INSERT INTO trees (approx_age, tree_type_id, x, y, area_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [tree.approx_age, tree.tree_type.id, tree.x, tree.y, tree.area.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    tree.id = id
    return tree

def select_all():
    pass


def delete_all():
    sql = "DELETE FROM trees"
    run_sql(sql)

def select(id):
    pass

def delete(id):
    pass

def update(tree):
    pass