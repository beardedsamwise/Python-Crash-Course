class Restaurant():
	"""This class is a simple attempt to model a restaurant."""
	
	def __init__(self,restaurant_name,cuisine_type):
		"""Initilise restaurant name and cuisine type attributes."""
		
		self.name = restaurant_name
		self.cuisine = cuisine_type
		self.served = 0

	def describe_restaurant(self):
		"""This method describes the restaurant."""
		
		print('The restaurant is called ' + self.name.title() + 
			' and it serves ' + self.cuisine.title() + '.\n')

	def open_restaurant(self):
		"""This method opens the restaurant."""
		
		print(self.name.title() + " is now open!!!\n")

	def set_number_served(self,customers_served):
		"""This method sets the number of customers served."""

		self.served = customers_served
		print(self.name.title() + ' has now served ' + str(self.served) +
			' customers.\n'
			)

	def increment_number_served(self,customers_served):
		"""This method increments the number of customers served."""

		self.served += customers_served
		print(self.name.title() + ' has now served ' + str(self.served) +
			' customers.\n'
			)



restaurant1 = Restaurant('Shujinko','Ramen')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.set_number_served(10)
restaurant1.increment_number_served(44)

restaurant2 = Restaurant('hakata gensuke','ramen')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()


restaurant3 = Restaurant('oda sushi','sushi')
restaurant3.describe_restaurant()
restaurant3.open_restaurant()