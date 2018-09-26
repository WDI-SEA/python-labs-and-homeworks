def kwargosaurus(**kwargs):
  for dinosaur, size in kwargs.items():
    if dinosaur == "smaller":
      print(f'{dinosaur} is small! Mighty Kwargosaurus will fight you!')
    else:
      print(f'{dinosaur} is big! Whimpering Kwargosaurus cries and runs away!')

kwargosaurus(Velociraptor="smaller", Stegasaurus="smaller", Triceratops="smaller", Trex="bigger")
