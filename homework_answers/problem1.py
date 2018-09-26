contacts = {
  "Carly": "333-3333",
  "Blondie": "444-4444",
  "Jenny": "867-5309"
}
name = "Jenny"

def get_contact(contacts, name):
  for person in contacts:
    if person == name:
      return contacts[person]

phone_number = get_contact(contacts, name)

if phone_number:
  print("The phone number of", name, "is", phone_number)
else:
  print("That name isn't in your contacts list")

  