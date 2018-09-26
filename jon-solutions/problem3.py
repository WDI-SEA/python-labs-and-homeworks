class Animal:
    def __init__(self):
        print("I am coming to life!")
        self.energy = 50

    def eat(self, amount):
        self.energy += amount
        print("My energy level is ", self.energy)

    def move(self):
        self.energy -= 10
        print("I am running!")

    def get_status(self):
        if self.energy > 100:
            print("I'm feeling stuffed")
        elif 50 <= self.energy and self.energy < 100: 
            print("I'm happily full.")
        elif 0 <= self.energy and self.energy < 50:
            print("I'm starving!")
        else:
            print("I'm dead :(")

    def say_hi(self):
        print("Meep!")


print("Making my first animal")
first_animal = Animal()
first_animal.get_status()
first_animal.eat(55)
first_animal.get_status()
first_animal.move()
first_animal.get_status()
print("first animal saying hi")
first_animal.say_hi()
print()

print("Making a second animal now")
second_animal = Animal()
second_animal.get_status()
second_animal.eat(-45)
second_animal.get_status()
second_animal.move()
second_animal.get_status()
print("second animal saying hi")
second_animal.say_hi()