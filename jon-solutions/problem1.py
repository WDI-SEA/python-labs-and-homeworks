contacts = {
  "Carly": "333-3333",
  "Blondie": "444-4444",
  "Jenny": "867-5309"
}

name = "Jenny"

def get_contact(dictionary, person):
    for contact_name, phone_num in dictionary.items():
        if (contact_name == person):
            return phone_num

phone_number = get_contact(contacts, name)
print("The phone number of", name, "is", phone_number)
