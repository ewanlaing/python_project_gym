class Member:
    def __init__(self, name, premium, active, id = None):
        self.name = name
        self.premium = premium
        self.active = active
        self.id = id

    def deactivate_member(self):
        self.active = False

    def activate_member(self):
        self.active = True