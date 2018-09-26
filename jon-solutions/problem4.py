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


class Penguin(Animal):
    def __init__(self):
        super().__init__()
        print("I am a penguin!")
        self.energy = 100

    def move(self):
        self.energy -= 5
        print("I'm sliding!")

class Eagle(Animal):
    def __init__(self):
        super().__init__()
        print("I am an eagle!")
        self.energy = 20

    def move(self):
        if self.energy > 0:
            self.energy -= 20
            print("I'm flying to the sea!")
        else:
            print("I'm too tired to fly")

    def say_hi(self):
        print("Shrieek!")

animal = Animal()
animal.get_status()
animal.eat(60)
animal.get_status()
animal.move()
animal.get_status()
animal.say_hi()
print()

penguin = Penguin()
penguin.eat(5)
penguin.get_status()
penguin.move()
penguin.get_status()
penguin.say_hi()
print()

eagle = Eagle()
eagle.say_hi()
eagle.get_status()
eagle.move()
eagle.get_status()
eagle.move()
eagle.get_status()
eagle.move()
print()