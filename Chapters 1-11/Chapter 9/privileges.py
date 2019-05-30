class Privileges():
	"""This class defines the privileges for a user."""
	def __init__(self,privileges=[]):
		self.privileges = privileges

	def show_privileges(self):
		"""This method will display a list of the Admin user's privileges."""

		print("This Admin user has these privileges:")
		for privilege in self.privileges:
			print("- " + privilege.title())