def city_country(city, country):
	"""Returns the city and country as a neatly formatted string"""
	formatted_location = '"' + city + ', ' + country + '"'
	return formatted_location.title()

location = city_country('melbourne','australia')
print(location)	