my_pizzas = ['hawaiian','margarita','americana']

friend_pizzas = my_pizzas[:]

my_pizzas.append('vegetarian')

friend_pizzas.append('meat lovers')

print("My favourite pizzas are:")
for pizza in my_pizzas:
	print(pizza)

print("\n")

print("My friends favourite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)


