from flask import render_template, request, redirect, Blueprint
from models.workout import Workout
from models.g_class import G_class
from models.member import Member
import repositories.g_class_repository as g_class_repository
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository

g_classes_blueprint = Blueprint("g_classes", __name__)

@g_classes_blueprint.route("/classes/index")
def home():
    return render_template("/classes/index.html")