class Human :
    leg_count = 4
    gender = "Unknown"

    def get_gender(self, gender):
            self.gender = gender

human = Human()
print(human.gender)


class Man(Human):
    race = "Black"

Man1 = Man

print(Man1.race, Man1.gender)










