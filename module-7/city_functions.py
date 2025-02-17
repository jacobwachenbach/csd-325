# Jacob W. Achenbach Module 7.2 Assignment
# city_functions.py

# This file formats a city and country name into a capitalized string, then called three times showing each city and country population

def city_country(city, country, population=None, language=None):
    #Return a formatted city and country name.
    formatted_string = f"{city.title()}, {country.title()}"
    if population:
        formatted_string += f" - population {population}"
    if language:
        formatted_string += f", {language.title()}"
    return formatted_string

# Calling the function three times
print(city_country("santiago", "chile"))
print(city_country("paris", "france", population=2148000))
print(city_country("tokyo", "japan", population=13929286, language="japanese"))
