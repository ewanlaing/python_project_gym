class G_class:
    def __init__(self, name, date, time, duration, capacity, members, active, id = None):
        self.name = name
        self.date = date
        self.time = time
        self.duration = duration
        self.capacity = capacity
        self.members = members
        self.active = active
        self.id = id

    def deactivate_g_class(self):
        self.active = False

    def activate_g_class(self):
        self.active = True