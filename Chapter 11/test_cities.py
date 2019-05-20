from city_country import city_country
import unittest

class CityTestCase(unittest.TestCase):
    """Tests for 'test_cities.py'."""

    def test_city_country(self):
        """Do locations like 'Melbourne, Australia' work?"""
        formatted_loc = city_country('melbourne','australia')
        self.assertEqual(formatted_loc, 'Melbourne, Australia')

    def test_population(self):
        """Do locations like 'Melbourne, Australia, 1000' work?"""
        formatted_loc = city_country('melbourne','australia','1000')
        self.assertEqual(formatted_loc, 'Melbourne, Australia, 1000')

unittest.main()