favorite_numbers = {
	'sam' : [42,55],
	'pepper' : [3,77,99],
	'roland' : [6,77],
	'edgar' : [1,88,7,8,100],
	}

# number = favorite_numbers['sam']
# print("Sam's favorite numbers are: " + str(number))

# number = favorite_numbers['pepper']
# print("Pepper's favorite numbers are: " + str(number))

# number = favorite_numbers['roland']
# print("Roland's favorite numbers are: " + str(number))

# number = favorite_numbers['edgar']
# print("Edgar's favorite numbers are: " + str(number))

for name, numbers in favorite_numbers.items():
	print("\n" + name.title() + "'s favourite numbers are:")
	for number in numbers:
		print("\t" + str(number))