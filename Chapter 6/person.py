alex = {
	'first_name' : 'alex',
	'last_name' : 'honnold',
	'age' : '32',
	'city' : 'yosemite',
	}

tommy = {
	'first_name' : 'tommy',
	'last_name' : 'caldwell',
	'age' : '42',
	'city' : 'yosemite',
	}

emily = {
	'first_name' : 'emily',
	'last_name' : 'harrington',
	'age' : '31',
	'city' : 'tahoe',
	}

people = [alex, tommy, emily]

#old code
# print(alex['first_name'])
# print(alex['last_name'])
# print(alex['age'])
# print(alex['city'])

for person in people:
	print("Full Name: " + person['first_name'].title() + " " + person['last_name'].title())
	print("Age: " + person['age'])
	print("Location: " + person['city'].title() + "\n")