cities = {
	'melbourne' : {
	'country' : 'australia',
	'population' : 4400000,
	'fact' : 'Capital of Victoria'
	},
	'tokyo' : {
	'country' : 'japan',
	'population' : 9200000,
	'fact' : 'Capital of Japan',
	},
	'auckland' : {
	'country' : 'new zealand',
	'population' : 1650000,
	'fact' : 'Largest urban area in New Zealand',
	}
}

for city, city_dict in cities.items():
	print("\n" + city.title() + ":")
	print("\t" + "City: " + city_dict['country'].title())
	print("\t" + "Population: " + str(city_dict['population']))
	print("\t" + "Fact: " + city_dict['fact'])