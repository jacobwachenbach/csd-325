# Jacob W. Achenbach Module 7.2 Assignment
# test_cities.py

# This file helps verify the cit and country names with population and language

import unittest
from city_functions import city_country

class TestCityFunctions(unittest.TestCase):
    """Tests for city_country function."""
    
    def test_city_country(self):
        """Does it work for city, country?"""
        formatted = city_country('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')
    
    def test_city_country_population(self):
        """Does it work for city, country, population?"""
        formatted = city_country('paris', 'france', population=2148000)
        self.assertEqual(formatted, 'Paris, France - population 2148000')
    
    def test_city_country_population_language(self):
        """Does it work for city, country, population, language?"""
        formatted = city_country('tokyo', 'japan', population=13929286, language='japanese')
        self.assertEqual(formatted, 'Tokyo, Japan - population 13929286, Japanese')

if __name__ == '__main__':
    unittest.main()
