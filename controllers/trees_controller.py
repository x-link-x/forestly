from flask import render_template, redirect, request
from flask import Blueprint 
from models.tree import Tree
import repositories.tree_repository as tree_repository
import repositories.area_repository as area_repository
import repositories.treetype_repository as treetype_repository

trees_blueprint = Blueprint('trees', __name__)

@trees_blueprint.route("/trees")
def trees():
    trees = tree_repository.select_all()
    return render_template("trees/index.html", trees=trees)

@trees_blueprint.route("/trees/new")
def new_tree():
    areas = area_repository.select_all()
    tree_types = treetype_repository.select_all()
    return render_template("trees/new.html", areas=areas, tree_types=tree_types)

@trees_blueprint.route("/trees", methods=["POST"])
def create_tree():
    approx_age = request.form["approx_age"]
    tree_type_id = request.form["treetype_id"]
    area_id = request.form["area_id"]
    tree_type = treetype_repository.select(tree_type_id)
    area = area_repository.select(area_id)
    x = request.form["x"]
    y = request.form["y"]
    tree = Tree(approx_age, tree_type, area, x, y)
    tree_repository.save(tree)
    return redirect("/trees")

