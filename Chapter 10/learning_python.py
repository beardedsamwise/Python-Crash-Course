filename = 'learning_python.txt'

#print contents by reading entire file
with open(filename) as file_object:
	contents = file_object.read()
print(contents)

#print contents by looping over file
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

#print contents by looping over variable stored externally to with block
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

