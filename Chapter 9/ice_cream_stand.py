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

class IceCreamStand(Restaurant):
	"""This class is a simple attempt to model an ice cream stand."""

	def __init___(self,restaurant_name,cuisine_type='ice_cream'):
		"""Init attributes of the parent class."""
		super().__init___(restaurant_name,cuisine_type)
		self.flavours = []

	def show_flavours(self):
		print("We have these flavours available:")
		for flavour in self.flavours:
			print("- " + flavour)

pidapipo = IceCreamStand('pidapipo')

pidapipo.describe_restaurant()