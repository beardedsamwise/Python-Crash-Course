from random import randint

class Die():
	"""This class simulates rolling a die"""

	def __init__(self,die_sides):
		"""Initiate attributes"""
		self.die_sides = die_sides

	def roll_dice(self):
		"""This method simulates the process of rolling a die"""
		x = randint(1, self.die_sides)
		print('You rolled a ' + str(x) + ' using a ' + str(self.die_sides)  +
		 ' sided die.\n')

six_sided = Die(6)
six_sided.roll_dice()

ten_sided = Die(10)
ten_sided.roll_dice()

twenty_sided = Die(20)
twenty_sided.roll_dice()
