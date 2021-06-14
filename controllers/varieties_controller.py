from flask import render_template, redirect, request
from flask import Blueprint 
from models.variety import Variety
import repositories.variety_repository as variety_repository

varieties_blueprint = Blueprint('varieties', __name__)

# INDEX
@varieties_blueprint.route("/varieties")
def varieties():
    varieties = variety_repository.select_all()
    return render_template("varieties/index.html", varieties=varieties)

# NEW
@varieties_blueprint.route("/varieties/new")
def new_variety():
    return render_template("varieties/new.html")

# CREATE
@varieties_blueprint.route("/varieties", methods=["POST"])
def create_variety():
    name = request.form['variety']
    variety = Variety(name)
    variety_repository.save(variety)
    return redirect("/varieties")

# SHOW
@varieties_blueprint.route("/varieties/<id>")
def show_variety(id):
    variety = variety_repository.select(id)
    trees = variety_repository.trees(variety)
    return render_template("varieties/show.html", variety=variety, trees=trees)

# EDIT
@varieties_blueprint.route("/varieties/<id>/edit")
def edit_variety(id):
    variety = variety_repository.select(id)
    return render_template("varieties/edit.html", variety=variety)

# UPDATE
@varieties_blueprint.route("/varieties/<id>", methods=["POST"])
def update_variety(id):
    name = request.form["name"]
    updated_variety = Variety(name, id)
    variety_repository.update(updated_variety)
    return redirect("/varieties")

# DELETE
@varieties_blueprint.route("/varieties/<id>/delete", methods=["POST"])
def delete_variety(id):
    variety_repository.delete(id)
    return redirect("/varieties")