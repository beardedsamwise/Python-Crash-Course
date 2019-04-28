programming_words = {
	'list' : 'A list is a collection of items in a particular order',
	'loop' : 'Looping allows you to take the same action, or a set of , ' \
	'actions with every item in a list',
	'tuple' : 'A tuple is a list with immutable items',
	'if statement' : 'An if statement allows you to examine and respond , ' \
	' to the state of a program',
	}

#old inefficient code
# word = 'list'
# print(word.title() + ": " + programming_words['list'])

# word = 'loop'
# print("\n" + word.title() + ": " + programming_words['loop'])

# word = 'tuple'
# print("\n" + word.title() + ": " + programming_words['tuple'])

# word = 'if statement'
# print("\n" + word.title() + ": " + programming_words['if statement'])

#new efficient code! 
for key, value in programming_words.items():
	print(key.title() + ": " + value + "\n")