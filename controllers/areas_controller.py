from flask import Flask, render_template, redirect, request
from flask import Blueprint 
from models.area import Area


areas_blueprint = Blueprint('area', __name__)