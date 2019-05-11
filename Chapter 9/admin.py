from privileges import Privileges
from user import User

class Admin(User):
	"""This class adds Admin user functionality to the User class."""

	def __init__(self,first_name,last_name,department,age):
		"""Init attributes of the parent class."""

		super().__init__(first_name,last_name,department,age)
		self.privileges = Privileges()



