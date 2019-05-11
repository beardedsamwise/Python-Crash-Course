filename = 'learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

c_string = ''

for line in lines:
	c_string += line.replace('Python','C')

print(c_string.rstrip())