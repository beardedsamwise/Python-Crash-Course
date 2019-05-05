responses = {}

poll_active = True

while poll_active:
	name = input("\nWhat is your name? ")
	destination = input("Where would you like to go on holiday? ")

	responses[name] = destination

	continue_prompt = input("Would you like query another person? (Yes/No) ")
	continue_prompt = continue_prompt.lower()
	if continue_prompt == "no":
		poll_active = False

print(" ")

for name, destination in responses.items():
	print(name.title() + " would like to go to " + destination.title() + ".")