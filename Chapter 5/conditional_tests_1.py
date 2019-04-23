#Conditional tests with strings

shoes = 'La Sportiva'

print("Are shoes == 'La Sportiva'? I predict True")
print(shoes == 'La Sportiva')

print("\nAre shoes == 'Nike'? I predict False")
print(shoes == 'Nike')

print("\nAre shoes != 'Nike'? I predict True")
print(shoes != 'Nike')

print("\nAre shoes != 'la sportiva'? I predict True")
print(shoes != 'la sportiva')

print("\nAre shoes == 'la sportiva' if we ignore the case? I predict True")
print(shoes.lower() == 'la sportiva')

#Conditional tests with numbers

number = 12

print("\nIs the number greater than 6?")
print(number > 6)

print("\nIs the number less than 6?")
print(number < 6)

print("\nIs the number divisable by 2 and 3 without a remainder?")
print(number % 2 == 0 and number % 3 == 0)

print("\nIs the number divisable by 4 or 5 without a remainder?")
print(number % 4 == 0 or number % 5 == 0)

print("\nIs the number divisable by 4 and 5 without a remainder?")
print(number % 4 == 0 and number % 5 == 0)

#Conditional tests with lists

list = ['pizza','donuts','pie']

print("\nIs pizza in the list?")
print('pizza' in list)

print("\nIs dumplings in the list?")
print('dumplings' in list)

print("\nIs pizza and pie in the list?")
print('pizza' in list and 'donuts' in list)

print("\nIs pizza, pie and burgers in the list?")
print('pizza' in list and 'donuts' in list and 'burgers' in list)