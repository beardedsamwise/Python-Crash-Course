class Employee():
    """This class models an employee and their salary"""

    def __init__(self,first,last,salary):
        """Initiate attributes"""
        self.name = first.title() + " " + last.title()
        self.salary = int(salary)
    
    def give_raise(self,promotion="5000"):
        """Gives employee raise, with default of $5000"""
        print(self.name + " earns $" + str(self.salary))
        print("Let's give them a raise of $" + str(promotion))
        self.salary = self.salary + int(promotion)
        print(self.name + " now earns $" + str(self.salary))


