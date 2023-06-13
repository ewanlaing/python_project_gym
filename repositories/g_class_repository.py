from db.run_sql import run_sql
from models.g_class import G_class
from models.member import Member
import repositories.workout_repository as workout_repository
import repositories.member_repository as member_repository

def save(g_class):
    sql = "INSERT INTO g_classes (name, date, time, duration, capacity, number_of_members, active) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [g_class.name, g_class.date, g_class.time, g_class.duration, g_class.capacity, len(g_class.members), g_class.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    g_class.id = id
    return g_class

def members_in_g_class(id):
    sql = "SELECT * FROM members INNER JOIN workouts ON workouts.member_id = members.id WHERE g_class_id = %s"
    values = [id]
    results = run_sql(sql, values)
    members = []
    for result in results:
        member = member_repository.select(result['member_id'])
        members.append(member)
    return members

def select_all():
    g_classes = []
    sql = "SELECT * FROM g_classes"
    results = run_sql(sql)

    for row in results:
        members = members_in_g_class(row['id'])
        g_class = G_class(row['name'], row['date'], row['time'], row['duration'], row['capacity'], members, row['active'], row['id'])
        g_classes.append(g_class)
    return g_classes

def select(id):
    g_class = None
    sql = "SELECT * FROM g_classes WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        members = members_in_g_class(result['id'])
        g_class = G_class(result['name'], result['date'], result['time'], result['duration'], result['capacity'], members, result['active'], result['id'])
    return g_class
    
def delete_all():
    sql = "DELETE FROM g_classes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM g_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(g_class):
    sql = "UPDATE g_classes SET (name, date, time, duration, capacity, number_of_members, active) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [g_class.name, g_class.date, g_class.time, g_class.duration, g_class.capacity, len(g_class.members), g_class.active, g_class.id]
    run_sql(sql, values)

