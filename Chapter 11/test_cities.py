from city_country import city_country
import unittest

#city_country('melbourne','australia')

class CityTestCase(unittest.TestCase):
    """Tests for 'test_cities.py'."""

    def test_city_country(self):
        """Do locations like 'Melbourne, Australia' work?"""
        formatted_loc = city_country('melbourne','australia')
        self.assertEqual(formatted_loc, 'Melbourne, Australia')

unittest.main()