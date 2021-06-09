from flask import Flask, render_template, redirect, request
from flask import Blueprint 
from models.area import Area
import repositories.area_repository as area_repository

areas_blueprint = Blueprint('area', __name__)

@areas_blueprint.route("/areas")
def areas():
    areas = area_repository.select_all()
    return render_template("areas/index.html", areas=areas)