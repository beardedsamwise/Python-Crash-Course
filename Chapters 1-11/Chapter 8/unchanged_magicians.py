def make_great(magicians):
	great_magicians = []

	while magicians:
		current_magician = magicians.pop().title() + ' the GREAT!'
		great_magicians.append(current_magician)
	for great_magician in great_magicians:
		print(great_magician)

def show_magicians(magicians):
	for magician in magicians:
		print(magician.title() + ' is a magician!')

magicians_list = ['harry houdini','david blaine','david copperfield']

make_great(magicians_list[:])

print('')

show_magicians(magicians_list)

