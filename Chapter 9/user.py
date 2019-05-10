class User():
	"""This is a simple attempt to model a user."""
	def __init__(self,first_name,last_name,department,age):
		"""Initilise users various attributes."""

		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.department = department.title()
		self.age = age
		self.login_attempts = 0

	def describe_user(self):
		"""This method describes the user."""

		print('The users name is: ' + self.first_name + 
			' ' + self.last_name
			)
		print(self.first_name + "'s age is: " + str(self.age))
		print(self.first_name + ' works in this department: ' + 
			self.department + '\n'
			)

	def greet_user(self):
		"""This method greets the user."""

		print('Hello ' + self.first_name + ', welcome to this Python ' +
			'script!\n'
			)

	def increment_login_attempts(self):
		"""This method increments the number of login attempts for a user"""

		self.login_attempts += 1
		print('FAILED LOGIN ATTEMPT!')
		print('Login attempts: ' + str(self.login_attempts) + '\n')

	def reset_login_attempts(self):
		"""This method increments the number of login attempts for a user"""

		self.login_attempts = 0
		print('*Login attempts have been reset*')
		print('Login attempts are now: ' + str(self.login_attempts) + '\n')

sam = User('sam','bentley','information technology','22')
sam.describe_user()
sam.greet_user()
sam.increment_login_attempts()
sam.reset_login_attempts()

peter = User('peter','griffin','drunk','45')
peter.describe_user()
peter.greet_user()

homer = User('homer','simpson','nuclear power plant','42')
homer.describe_user()
homer.greet_user()