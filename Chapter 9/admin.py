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

class Privileges():
	"""This class defines the privileges for a user."""
	def __init__(self,privileges=[]):
		self.privileges = privileges

	def show_privileges(self):
		"""This method will display a list of the Admin user's privileges."""

		print("This Admin user has these privileges:")
		for privilege in self.privileges:
			print("- " + privilege.title())

class Admin(User):
	"""This class adds Admin user functionality to the User class."""

	def __init__(self,first_name,last_name,department,age):
		"""Init attributes of the parent class."""

		super().__init__(first_name,last_name,department,age)
		self.privileges = Privileges()

Admin_User = Admin('Peter','Griffin','IT Dept',33)
Admin_User.privileges.privileges = [
'ban hammer',
'nuke user',
'be awesome'
]

Admin_User.describe_user()
Admin_User.privileges.show_privileges()

