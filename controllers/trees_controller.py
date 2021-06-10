from flask import Flask, render_template, redirect, request
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