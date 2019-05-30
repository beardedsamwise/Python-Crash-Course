magicians_list = ['harry houdini','david blaine','david copperfield']
great_magicians = []

def make_great(magicians):
	while magicians_list:
		current_magician = magicians_list.pop()
		print(current_magician.title() + ' is a GREAT magician!')
		great_magicians.append(current_magician)

def show_magicians(magicians):
	for magician in magicians:
		print(magician.title() + ' is a magician!')

show_magicians(magicians_list)
print('')

make_great(magicians_list)
show_magicians(magicians_list)

