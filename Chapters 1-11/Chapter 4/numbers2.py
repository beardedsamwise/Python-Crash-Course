#define and print list of odd numbers from 1-20
numbers = list(range(1,21,2))
for number in numbers:
	print (number)

#cube the numbers from 1-10 and then print the list of them
numbers = []

for value in range(1,11):
	cube = value**3
	numbers.append(cube)

print (numbers)

cubes = [value**3 for value in range(1,11)]
print (cubes)