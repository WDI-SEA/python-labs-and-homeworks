def kwargosaurus(**kwargs):
    for dinosaur, size in kwargs.items():
        if size == 'smaller':
            print(dinosaur, "is small! Mighty Kwargosaurus will fight you!")
        else:
            print(dinosaur, 'is big! Whimpering Kwargosaurus cries and runs away!')

kwargosaurus(Velociraptor="smaller", Stegosaurus="smaller", Triceratops="smaller", Trex="bigger")
