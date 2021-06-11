from flask import render_template, redirect, request
from flask import Blueprint 
from models.tree import Tree
import repositories.tree_repository as tree_repository
import repositories.area_repository as area_repository
import repositories.variety_repository as variety_repository

trees_blueprint = Blueprint('trees', __name__)

@trees_blueprint.route("/trees")
def trees():
    trees = tree_repository.select_all()
    return render_template("trees/index.html", trees=trees)

@trees_blueprint.route("/trees/new")
def new_tree():
    areas = area_repository.select_all()
    varieties = variety_repository.select_all()   
    return render_template("trees/new.html", areas=areas, varieties=varieties)

@trees_blueprint.route("/trees", methods=["POST"])
def create_tree():
    approx_age = request.form["approx_age"]
    variety_id = request.form["variety_id"]
    area_id = request.form["area_id"] 
    variety = variety_repository.select(variety_id)
    area = area_repository.select(area_id)
    x = request.form["x"]
    y = request.form["y"]
    tree = Tree(approx_age, variety, area, x, y)
    tree_repository.save(tree)
    return redirect("/trees")
