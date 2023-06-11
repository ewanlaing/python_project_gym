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

member1.premium = True
member_repository.update(member1)

member2 = Member('Sarah', False, False)
member_repository.save(member2)

member2.activate_member()
member_repository.update(member2)

member1.deactivate_member()
member_repository.update(member1)

members = [member1, member2]

g_class1 = G_class('Spin', '21.2.23', '3pm', '45 mins', 8, members, True)
g_class_repository.save(g_class1)

g_class2 = G_class('Body Pump', '25.3.23', '11am', '60 mins', 10, members, False)
g_class_repository.save(g_class2)

g_class2.activate_g_class()
g_class_repository.update(g_class2)

g_class1.deactivate_g_class()
g_class_repository.update(g_class1)


workout1 = Workout(member1.id, g_class1.id)
workout_repository.save(workout1)
workout2 = Workout(member2.id, g_class1.id)
workout_repository.save(workout2)