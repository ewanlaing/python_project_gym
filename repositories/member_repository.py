from db.run_sql import run_sql
from models.g_class import G_class
from models.member import Member
import repositories.workout_repository as workout_repository
import repositories.g_class_repository as g_class_repository

def save(member):
    sql = "INSERT INTO members (name, premium, active) VALUES (%s, %s, %s) RETURNING *"
    values = [member.name, member.premium, member.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['name'], row['premium'], row['active'], row['id'])
        members.append(member)

    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        member = Member(result['name'], result['premium'], result['active'], result['id'])
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(member):
    sql = "UPDATE members SET (name, premium, active) = (%s, %s, %s) WHERE id = %s"
    values = [member.name, member.premium, member.active, member.id]
    run_sql(sql, values)

def g_classes_for_member(id):
    sql = "SELECT * FROM g_classes INNER JOIN workouts ON workouts.g_class_id = g_classes.id WHERE member_id = %s"
    values = [id]
    results = run_sql(sql, values)
    g_classes = []
    for result in results:
        g_class = g_class_repository.select(result['g_class_id'])
        g_classes.append(g_class)
    return g_classes

    