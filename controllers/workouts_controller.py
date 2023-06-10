from flask import render_template, request, redirect, Blueprint
from models.workout import Workout
from models.g_class import G_class
from models.member import Member
import repositories.g_class_repository as g_class_repository
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository

workouts_blueprint = Blueprint("workouts", __name__)

@workouts_blueprint.route("/")
def home():
    return render_template("/index.html")
