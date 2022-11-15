class Animal :
    sound = 'mheem'

    def get_sound(self, sound):
            self.sound = sound

class Cat(Animal) :
    kitten_sound = 'Meow'

class Dog(Animal) :
    puppy_sound = "Hoooo"

cat = Cat()
print(cat.kitten_sound)

dog = Dog()
print(dog.puppy_sound)


