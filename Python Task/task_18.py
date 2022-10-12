class Human:
    leg_count = 4
    can_walk = True

    def __init__(self):
        self.name = "unknown"

human = Human()

print(human.name, human.can_walk)
