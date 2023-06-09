from models.member import Member
from models.g_class import G_class
from models.workout import Workout

import repositories.member_repository as member_repository
import repositories.g_class_repository as g_class_repository
import repositories.workout_repository as workout_repository

workout_repository.delete_all()
g_class_repository.delete_all()
member_repository.delete_all()

member1 = Member('Ewan', False, True)
member_repository.save(member1)

member2 = Member('Sarah', False, True)
member_repository.save(member2)

members = [member1, member2]

g_class1 = G_class('Spin', '21.2.23', '3pm', 45, 8, members, True)
g_class_repository.save(g_class1)