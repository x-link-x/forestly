from flask import Flask, render_template, redirect, request
from flask import Blueprint 
from models.area import Area
import repositories.area_repository as area_repository

areas_blueprint = Blueprint('area', __name__)

@areas_blueprint.route("/areas")
def areas():
    areas = area_repository.select_all()
    return render_template("areas/index.html", areas=areas)


@areas_blueprint.route("/areas/new")
def new_area():
    return render_template("areas/new.html")

@areas_blueprint.route("/areas", methods=["POST"])
def create_area():
    easting = request.form["easting"]
    northing = request.form["northing"]
    area = Area(easting, northing)
    area_repository.save(area)
    return redirect("/areas")


@areas_blueprint.route("/areas/<id>")
def show_area(id):
    area = area_repository.select(id)
    trees = area_repository.trees()
    return render_template("areas/show.html", area=area, trees=trees)

@areas_blueprint.route("/areas/<id>/edit")
def edit_area(id):
    area = area_repository.select(id)
    return render_template("areas/edit.html")