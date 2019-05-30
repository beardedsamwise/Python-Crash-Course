prompt = "\nEnter your age to check ticket prices."
prompt += "\nEnter quit to finish checking prices."
prompt += "\nAge: "

active = True

while active:
	age = input(prompt)
	if age == 'quit':
		active = False
	else:
		age = int(age)
		if age < 3:
			print("Under the age of 3: Your movie ticket is free!")
		elif age < 12:
			print("Between the age of 3 and 12: Your movie ticket is $10")
		else:
			print("Age 12 or over: Your movie ticket is $15")