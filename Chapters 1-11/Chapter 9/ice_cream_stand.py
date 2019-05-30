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

	def __init__(self,restaurant_name,cuisine_type='ice cream'):
		"""Init attributes of the parent class."""
		super().__init__(restaurant_name,cuisine_type)
		self.flavours = []

	def show_flavours(self):
		"""Display the flavours available at the ice cream stand."""
		print("We have these flavours available:")
		for flavour in self.flavours:
			print("- " + flavour.title())

pidapipo = IceCreamStand('pidapipo')
pidapipo.flavours = ['chocolate','vanilla']

pidapipo.describe_restaurant()
pidapipo.show_flavours()