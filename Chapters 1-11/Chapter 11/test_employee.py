import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for class Employee"""

    def setUp(self):
        """Create instance for use in all test methods"""
        self.sam = Employee('Sam','Bentley',10000)
    
    def test_default_raise(self):
        """Test giving raise with default value"""
        self.sam.give_raise()
        self.assertEqual(self.sam.salary, 15000)

    def test_nondefault_raise(self):
        """Test giving raise with non default value"""
        self.sam.give_raise(10000)
        self.assertEqual(self.sam.salary, 20000)

unittest.main()