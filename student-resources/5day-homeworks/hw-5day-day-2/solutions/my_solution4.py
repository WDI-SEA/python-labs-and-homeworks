class Animal:
	def __init__(self):
		print('I am coming to life!')
		self.energy = 50
	
	def eat(self,amount):
		self.energy += amount

	def move(self):
		self.energy -= 10
		print('I am running!')

	def get_status(self):
		message = ''
		if (self.energy < 0):
			message = "I'm starving!"
		elif (self.energy in range (0,50)):
			message = "I'm getting hungry!"
		elif (self.energy in range (50, 101)):
			message = "I'm happily full."
		else:
			message = "I'm feeling stuffed!"
		print(f'Current energy is {self.energy}.')
		print(message)

	def say_hi(self):
		print('Meep!')

class Penguin(Animal):
	def __init__(self):
		super().__init__()
		self.energy = 100
		print("I am a penguin!")

	def move(self):
		self.energy -= 20
		print("I am sliding!")

class Eagle(Animal):
	def __init__(self):
		super().__init__()
		self.energy = 20

	def say_hi(self):
		print("shrieeeek!")

	def move(self):
		self.energy -= 20
		if (self.energy < 0):
			print("I'm too tired to fly...")
		else:
			print("I am flying to the sea!")

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