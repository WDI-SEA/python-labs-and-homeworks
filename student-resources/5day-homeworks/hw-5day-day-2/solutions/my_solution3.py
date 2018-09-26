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
