class Animal:
  def __init__(self):
    print('I am coming to life!')
    self.energy = 50

  def eat(self, amount):
    self.energy += amount

  def move(self):
    print('I am running!')
    self.energy -= 10

  def get_status(self):
    print('My energy level is', self.energy)
    if self.energy <= 50:
      print('I\'m starving!')
    elif 50 < self.energy <= 100:
      print('I\'m happily full.')
    else:
      print('I\'m feeling stuffed!')

  def say_hi(self):
    print('Meep!')
