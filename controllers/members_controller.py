from flask import render_template, request, redirect, Blueprint
from models.workout import Workout
from models.g_class import G_class
from models.member import Member
import repositories.g_class_repository as g_class_repository
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members/index", methods=['GET'])
def home():
    members = member_repository.select_all()
    return render_template("/members/index.html", members=members)

@members_blueprint.route("/members/add", methods=['GET'])
def add():
    return render_template("/members/add.html")

@members_blueprint.route("/members/index", methods=['POST'])
def create_member():
    name = request.form['name']
    if request.form['membership'] == 'premium':
        premium = True
    else:
        premium = False
    active = True
    member = Member(name, premium, active)
    member_repository.save(member)
    return redirect('/members/index')
