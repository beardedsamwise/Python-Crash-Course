class Restaurant():
	"""This method is a simple attempt to model a restaurant."""
	
	def __init__(self,restaurant_name,cuisine_type):
		"""Initilise restaurant name and cuisine type attributes."""
		self.name = restaurant_name
		self.cuisine = cuisine_type

	def describe_restaurant(self):
		"""This method describes the restaurant."""
		print('The restaurant is called ' + self.name.title() + 
			' and serves ' + self.cuisine.title() + '.')

	def open_restaurant(self):
		"""This method opens the restaurant."""
		print(self.name.title() + " is now open!!!")

my_restaurant = Restaurant('Shujinko','Ramen')

print(my_restaurant.name)
print(my_restaurant.cuisine + "\n") 

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()