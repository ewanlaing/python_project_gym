from db.run_sql import run_sql
from models.g_class import G_class
from models.member import Member
from models.workout import Workout
import repositories.member_repository as member_repository
import repositories.g_class_repository as g_class_repository

def save(workout):
    sql = "INSERT INTO workouts (member_id, g_class_id) VALUES (%s, %s) RETURNING *"
    values = [workout.member_id, workout.g_class_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    workout.id = id
    return workout

def select_all():
    workouts = []
    sql = "SELECT * FROM workouts"
    results = run_sql(sql)
    for row in results:
        workout = Workout(row['member_id'], row['g_class_id'], row['id'])
        workouts.append(workout)
    return workouts

def select(id):
    workout = None
    sql = "SELECT * FROM workouts WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        workout = Workout(result['member_id'], result['g_class_id'], result['id'])
    return workout

def delete_all():
    sql = "DELETE FROM workouts"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM workouts WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(workout):
    sql = "UPDATE workouts SET (member_id, g_class_id) = (%s, %s) WHERE id = %s"
    values = [workout.member_id, workout.g_class_id, workout.id]
    run_sql(sql, values)

