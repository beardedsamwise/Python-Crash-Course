class Restaurant():
	"""This class is a simple attempt to model a restaurant."""
	
	def __init__(self,restaurant_name,cuisine_type):
		"""Initilise restaurant name and cuisine type attributes."""
		self.name = restaurant_name
		self.cuisine = cuisine_type

	def describe_restaurant(self):
		"""This method describes the restaurant."""
		print('The restaurant is called ' + self.name.title() + 
			' and it serves ' + self.cuisine.title() + '.\n')

	def open_restaurant(self):
		"""This method opens the restaurant."""
		print(self.name.title() + " is now open!!!\n")

# restaurant1 = Restaurant('Shujinko','Ramen')
