pets = [
	{
	'name' : 'kita',
	'breed' : 'shiba inu',
	'owner' : 'sam',
	},
	{
	'name' : 'bento',
	'breed' : 'shiba inu',
	'owner' : 'tiffany'
	},
	{	
	'name' : 'fuji',
	'breed' : 'shiba inu',
	'owner' : 'sam',
	}
]

#print(pets)

for pet_dict in pets:
	print("\nHere's what I know about " + pet_dict['name'].title() + ":")
	for k, v in pet_dict.items():
		print("\t" + k.title() + ": " + v.title())