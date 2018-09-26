def get_contact(contacts, name):
	if name in contacts:
		print(f'The phone number of {name} is {contacts[name]}')
	else:
		print(f'{name} is not in the contacts')

contacts = {
  "Carly": "333-3333",
  "Blondie": "444-4444",
  "Jenny": "867-5309"
}

phone_number = get_contact(contacts, 'Jenny')
phone_number = get_contact(contacts, 'Carly')
phone_number = get_contact(contacts, 'Blondie')
phone_number = get_contact(contacts, 'Justin')


# If you would like to test the example code, uncomment the code below

# contacts = {
#   "Carly": "333-3333",
#   "Blondie": "444-4444",
#   "Jenny": "867-5309"
# }
# name = "Jenny"
# phone_number = get_contact(contacts, name)

# print("The phone number of", name, "is", phone_number)
