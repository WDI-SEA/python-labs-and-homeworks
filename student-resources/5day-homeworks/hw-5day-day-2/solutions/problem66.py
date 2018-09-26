def kwargosaurus(**kwargs):
    for key, value in kwargs.items():
        if value == "smaller":
            print(key, "is small! Mighty Kwargosaurus will fight you!")
        elif value == "bigger":
            print(key, "is big! Whimpering Kwargosaurus cries and runs away!")

kwargosaurus(Velociraptor="smaller", Stegosaurus="smaller", Triceratops="smaller", Trex="bigger")
