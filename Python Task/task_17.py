class Human:
    color = "Black"
    race = "African"

    def get_color_race(self):
        return self.color + ":" + self.race


human = Human()
print(human.color, human.race)
