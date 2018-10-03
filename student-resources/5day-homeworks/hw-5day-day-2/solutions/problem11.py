def get_contact(contacts, name):
    if "Jenny" in contacts:
        return contacts["Jenny"]

contacts = {
  "Carly": "333-3333",
  "Blondie": "444-4444",
  "Jenny": "867-5309"
}
name = "Jenny"

phone_number = get_contact(contacts, name)
print("The phone number of", name, "is", get_contact(contacts, name))




