# Jacob Achenbach Module 9.2 2/23/2025

# Take a api and a prompt to pull a given city's weather

import requests  # Import requests module to make API calls

# OpenWeatherMap API key
API_KEY = "API_KEY"

# Base URL for OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    # Fetches weather data for a given city using OpenWeatherMap API.
    # Displays weather description, temperature, humidity, and wind speed.
    
    
    # API request parameters
    params = {
        "q": city,           # City name input from user
        "appid": API_KEY,    # API key for authentication
        "units": "imperial"  # Use Fahrenheit for temperature
    }

    # Make a GET request to fetch weather data
    response = requests.get(BASE_URL, params=params)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Convert response to JSON format
        
        # Extract weather details from the API response
        weather_desc = data["weather"][0]["description"]  # Weather description
        temperature = data["main"]["temp"]  # Temperature in Fahrenheit
        humidity = data["main"]["humidity"]  # Humidity percentage
        wind_speed = data["wind"]["speed"]  # Wind speed in mph
        
        # Print weather details
        print(f"\nWeather in {city.capitalize()}:")
        print(f" - Description: {weather_desc.capitalize()}")  # Capitalize description
        print(f" - Temperature: {temperature}°F")  # Temperature in Fahrenheit
        print(f" - Humidity: {humidity}%")  # Humidity percentage
        print(f" - Wind Speed: {wind_speed} mph\n")  # Wind speed in mph
    
    else:
        # Error message if city name is incorrect or API call fails
        print("\nError fetching weather data. Please check the city name and try again.\n")

# Main function to run the script
if __name__ == "__main__":
    city_name = input("Enter a city: ").strip()  # Get city name from user input
    get_weather(city_name)  # Call the function to fetch and display weather
