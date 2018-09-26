def kwargosaurus(**kwargs):
  for dino, size in kwargs.items():
    if size == 'smaller':
      print(f'{dino} is {size}! Mighty Kwargosaurus will fight you!')
    else:
      print(f'{dino} is {size}! Whimpering Kwargosaurus cries and runs away!')

kwargosaurus(Velociraptor="smaller", Stegosaurus="smaller", Triceratops="smaller", Trex="bigger")