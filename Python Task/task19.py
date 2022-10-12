class Human:
    leg_count = 4
    can_walk = True
    describe = "This is Human"

    def __init__(self):
        self.name = "Black"

    def get_description(self, describe):
        self.describe = describe

    def get_let_count(self, leg_count):
        self.leg_count = leg_count

human = Human()
print(human.describe)
print("Leg Count: ", human.leg_count)




