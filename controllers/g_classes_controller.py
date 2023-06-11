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
    g_classes = g_class_repository.select_all()
    g_classes.sort(key=lambda x: x.date)
    return render_template("/classes/index.html", g_classes=g_classes)

@g_classes_blueprint.route("/classes/add", methods=['GET'])
def add():
    times = ['8am', '8.30am', '9am', '9.30am', '10am', '10.30am', '11am', '11.30am', '12 noon', '12.30pm', '1pm', '1.30pm', '2pm', '2.30pm', '3pm', '3.30pm', '4pm', '4.30pm', '5pm', '5.30pm', '6pm', '6.30pm', '7pm', '7.30pm', '8pm', '8.30pm']
    classes = ['Body Attack', 'Body Balance', 'Body Pump', 'FT Fit', 'Kickboxing', 'Spin', 'Yoga', 'Zumba']
    durations = ['30 mins', '45 mins', '60 mins']
    capacities = [10, 15, 20]
    return render_template("/classes/add.html", times=times, classes=classes, durations=durations, capacities=capacities)

@g_classes_blueprint.route("/classes/index", methods=['POST'])
def create_class():
    name = request.form.get('class')
    date = request.form.get('date')
    time = request.form.get('time')
    duration = request.form.get('duration')
    capacity = int(request.form.get('capacity'))
    members = []
    active = True
    g_class = G_class(name, date, time, duration, capacity, members, active)
    g_class_repository.save(g_class)
    return redirect('/classes/index')

@g_classes_blueprint.route("/classes/<id>/view", methods=['GET'])
def view(id):
    g_class = g_class_repository.select(id)
    return render_template("/classes/view.html", g_class=g_class)

@g_classes_blueprint.route("/classes/<id>/edit", methods=['GET'])
def edit(id):
    g_class = g_class_repository.select(id)
    times = ['8am', '8.30am', '9am', '9.30am', '10am', '10.30am', '11am', '11.30am', '12 noon', '12.30pm', '1pm', '1.30pm', '2pm', '2.30pm', '3pm', '3.30pm', '4pm', '4.30pm', '5pm', '5.30pm', '6pm', '6.30pm', '7pm', '7.30pm', '8pm', '8.30pm']
    classes = ['Body Attack', 'Body Balance', 'Body Pump', 'FT Fit', 'Kickboxing', 'Spin', 'Yoga', 'Zumba']
    durations = ['30 mins', '45 mins', '60 mins']
    capacities = [10, 15, 20]
    return render_template("classes/edit.html", g_class=g_class, times=times, classes=classes, durations=durations, capacities=capacities)

@g_classes_blueprint.route("/classes/<id>", methods=['POST'])
def update_class(id):
    name = request.form.get('class')
    date = request.form.get('date')
    time = request.form.get('time')
    duration = request.form.get('duration')
    capacity = int(request.form.get('capacity'))
    members = []
    status = request.form.get('status')
    if status == "active":
        active = True
    else:
        active = False
    g_class = G_class(name, date, time, duration, capacity, members, active, id)
    g_class_repository.update(g_class)
    return redirect('/classes/index')

@g_classes_blueprint.route("/classes/<id>/delete", methods=['POST'])
def delete_class(id):
    g_class_repository.delete(id)
    return redirect('/classes/index')
