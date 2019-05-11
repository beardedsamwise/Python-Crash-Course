from collections import OrderedDict

programming_words = OrderedDict()


programming_words = {
	'list' : 'A list is a collection of items in a particular order',
	'loop' : 'Looping allows you to take the same action, or a set of ' \
	'actions with every item in a list',
	'tuple' : 'A tuple is a list with immutable items',
	'if statement' : 'An if statement allows you to examine and respond' \
	' to the state of a program',
	}

for key, value in programming_words.items():
	print(key.title() + ": " + value + "\n")