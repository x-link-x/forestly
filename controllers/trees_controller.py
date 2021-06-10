from flask import Flask, render_template, redirect, request
from flask import Blueprint 
from models.tree import Tree
import repositories.tree_repository as tree_repository

trees_blueprint = Blueprint('trees', __name__)

@trees_blueprint.route('/trees')
def trees():
    trees = tree_repository.select_all()
    return render_template("trees/index.html", trees=trees)