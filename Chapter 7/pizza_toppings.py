prompt = "\nTell me what toppings you'd like on your pizza."
prompt += "\nEnter quit to when you've finished selecting your toppings."
prompt += "\nTopping selection: "

toppings = " "
while toppings != 'quit':
	toppings = input(prompt)
	print(toppings)
