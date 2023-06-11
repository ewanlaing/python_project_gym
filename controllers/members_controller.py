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
    members.sort(key=lambda x: x.name)
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

@members_blueprint.route("/members/<id>/view", methods=['GET'])
def view(id):
    member = member_repository.select(id)
    return render_template("members/view.html", member=member)

@members_blueprint.route("/members/<id>/edit", methods=['GET'])
def edit(id):
    member = member_repository.select(id)
    return render_template("/members/edit.html", member=member)

@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    old_member = member_repository.select(id)
    name = request.form['name']

    if old_member.premium == True:
        if request.form.get('standard'):
            premium = False
        else:
            premium = True
    if old_member.premium == False:
        if request.form.get('premium'):
            premium = True
        else:
            premium = False

    if old_member.active == True:
        if request.form.get('deactivate'):
            active = False
        else:
            active = True
    if old_member.active == False:
        if request.form.get('activate'):
            active = True
        else:
            active = False

    member = Member(name, premium, active, id)
    member_repository.update(member)
    return redirect('/members/index')

@members_blueprint.route("/members/<id>/delete", methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect('/members/index')

@members_blueprint.route("/members/<id>/book", methods=['GET'])
def book_class(id):
    member = member_repository.select(id)
    g_classes = g_class_repository.select_all()
    return render_template("/members/book.html", member=member, g_classes=g_classes)
