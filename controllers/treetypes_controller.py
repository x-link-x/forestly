from flask import Flask, render_template, redirect, request
from flask import Blueprint 
from models.treetype import TreeType
import repositories.treetype_repository as treetype_repository

treetypes_blueprint = Blueprint('tree_type', __name__)

