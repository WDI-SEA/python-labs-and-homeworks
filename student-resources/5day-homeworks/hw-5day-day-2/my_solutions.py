#QUESTION 1

contacts = {
  "Carly": "333-3333",
  "Blondie": "444-4444",
  "Jenny": "867-5309"
}
name = "Jenny"

def get_contact(contacts, name):
	return contacts[name]

phone_number = get_contact(contacts, name)

print("The phone number of", name, "is", phone_number)



#QUESTION 2

dict = {}

def letter_counter(string):
	for letter in string:
		if letter in dict:
			dict[letter] += 1
		else: 	
			dict[letter] = 1
	return(dict)		

print(letter_counter("abracdabra"))		


#QUESTION 3

class Animal:
	def __init__(self):
		self.energy=50
		print("I am coming to life!")

	def eat(self, amount):
		self.energy += amount


	def move(self):
		self.energy -=	10
		print("I am running!")	
		print("My energy level is", self.energy)	

	def get_status(self):
		if self.energy < 50:
			print("My energy level is", self.energy)
			print("I'm starving")
		elif self.energy <= 100:
			print("My energy level is", self.energy)
			print("I'm happily full")
		else:
			print("My energy level is", self.energy)
			print("I'm feeling stuffed!") 		

	def say_hi(self):
		print("meep")

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


#QUESTION 4

class Penguin(Animal):
	def __init__(self):
		super().__init__()
		self.energy=100
		print("I love Sidney Crosby!")

	def move(self):
		self.energy -=	5
		print("I am sliding!")	


class Eagle(Animal):
	def __init__(self):
		super().__init__()
		self.energy=20
		print("Ovi is the best!")

	def move(self):
		if self.energy > 0:
			self.energy -=	20
			print("I am flying to the sea!")
		else:
			print("I'm too tired to fly")

	def say_hi(self):
		print("shrieeeeeek!")	

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


# QUESTION 5

spices_onhand = ['cumin', 'nutmeg', 'salt', 'cumin', 'star anise', 'salt', 'basil', 'nutmeg', 'cumin', 'paprika', 'curry powder', 'pepper', 'curry powder', 'curry powder', 'cayenne', 'cumin', 'star anise', 'star anise', 'curry powder', 'salt', 'salt', 'cardamom', 'cayenne', 'star anise', 'chili powder', 'curry powder', 'thyme', 'thyme', 'cayenne', 'nutmeg', 'basil', 'star anise', 'chili powder', 'oregano', 'coriander', 'nutmeg', 'chili powder', 'coriander', 'paprika', 'pepper', 'thyme', 'nutmeg', 'paprika', 'cayenne', 'basil', 'cinnamon', 'curry powder', 'cardamom', 'star anise', 'pepper', 'salt', 'curry powder', 'thyme', 'cardamom', 'salt', 'pepper', 'paprika', 'salt', 'cinnamon', 'cumin', 'curry powder', 'cardamom', 'cumin', 'cardamom', 'oregano', 'cardamom', 'pepper', 'star anise', 'pepper', 'cayenne', 'chili powder', 'cardamom', 'nutmeg', 'pepper', 'cardamom', 'curry powder', 'thyme', 'basil', 'nutmeg', 'coriander', 'paprika', 'curry powder', 'cayenne', 'cumin', 'nutmeg', 'paprika', 'star anise', 'thyme', 'curry powder', 'cardamom', 'oregano', 'basil', 'cinnamon', 'oregano', 'coriander', 'curry powder', 'cumin', 'thyme', 'pepper', 'thyme', 'cardamom', 'cayenne', 'chili powder', 'basil', 'pepper', 'cumin', 'thyme', 'cardamom', 'star anise', 'cayenne', 'cinnamon', 'cinnamon', 'cinnamon', 'cardamom', 'curry powder', 'curry powder', 'pepper', 'chili powder', 'pepper', 'cinnamon', 'cardamom', 'basil', 'thyme', 'cinnamon', 'cumin', 'nutmeg', 'cinnamon', 'cayenne', 'cardamom', 'nutmeg', 'cardamom', 'paprika', 'cumin', 'cayenne', 'chili powder', 'cinnamon', 'cumin', 'star anise', 'cardamom', 'thyme', 'basil', 'paprika', 'basil', 'oregano', 'cardamom', 'pepper', 'oregano', 'nutmeg', 'nutmeg', 'salt', 'basil', 'cayenne', 'oregano', 'star anise', 'star anise', 'oregano', 'salt', 'pepper', 'cinnamon', 'basil', 'salt', 'cardamom', 'cayenne', 'oregano', 'cinnamon', 'pepper', 'cumin', 'thyme', 'thyme', 'oregano', 'oregano', 'star anise', 'paprika', 'thyme', 'cinnamon', 'cinnamon', 'oregano', 'star anise', 'oregano', 'chili powder', 'cayenne', 'oregano', 'cumin', 'paprika', 'nutmeg', 'star anise', 'coriander', 'star anise', 'nutmeg', 'chili powder', 'star anise', 'paprika', 'salt', 'salt', 'cayenne', 'curry powder', 'thyme', 'oregano', 'curry powder', 'curry powder']

spices_needed = set({"salt", "pepper", "ginger", "oregano", "paprika", "basil", "curry powder", "cumin", "cayenne", "lemon pepper", "chili powder", "nutmeg", "cinnamon", "star anise", "garlic salt", "coriander", "cardamom", "thyme"})


set(spices_onhand)

to_buy = (spices_needed.difference(spices_onhand)) 


print("Go shopping for", to_buy)


# QUESTION 6

def kwargosaurus(**kwargs):
	for keyword, size in kwargs.items():
		if size == "smaller":
			print(keyword, "is small! Mighty Kwargosaurus will fight you!")
		else:
			print(keyword, "is big! Whimpering Kwargosaurus cries and runs away!")		

kwargosaurus(Velociraptor="smaller", Stegosaurus="smaller", Triceratops="smaller", Trex="bigger")


