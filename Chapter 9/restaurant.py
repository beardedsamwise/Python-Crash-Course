class Restaurant():
	"""This class is a simple attempt to model a restaurant."""
	
	def __init__(self,restaurant_name,cuisine_type):
		"""Initilise restaurant name and cuisine type attributes."""
		self.name = restaurant_name
		self.cuisine = cuisine_type

	def describe_restaurant(self):
		"""This method describes the restaurant."""
		print('The restaurant is called ' + self.name.title() + 
			' and it serves ' + self.cuisine.title() + '.')

	def open_restaurant(self):
		"""This method opens the restaurant."""
		print(self.name.title() + " is now open!!!")

restaurant1 = Restaurant('Shujinko','Ramen')

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

print('')

restaurant2 = Restaurant('hakata gensuke','ramen')

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

print('')

restaurant3 = Restaurant('oda sushi','sushi')

restaurant3.describe_restaurant()
restaurant3.open_restaurant()