from flask import Flask, render_template, redirect, request
from flask import Blueprint 
from models.treetype import TreeType
import repositories.treetype_repository as treetype_repository

treetypes_blueprint = Blueprint('tree_type', __name__)

@treetypes_blueprint.route("/treetypes")
def treetypes():
    tree_types = treetype_repository.select_all()
    return render_template("tree_types/index.html", tree_types=tree_types)


@treetypes_blueprint.route("/treetypes/new")
def new_treetype():
    return render_template("tree_types/new.html")