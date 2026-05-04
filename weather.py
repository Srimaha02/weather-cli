import requests
import sys
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Get city from terminal argument
city = sys.argv[1] if len(sys.argv) > 1 else "Chennai"

# Build the API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Call the API
response = requests.get(url)
data = response.json()

# Check if city was found
if data.get("cod") != 200:
    print(f"City '{city}' not found. Try again.")
    sys.exit()

# Extract the data
temp      = data["main"]["temp"]
humidity  = data["main"]["humidity"]
wind      = data["wind"]["speed"]
condition = data["weather"][0]["description"].capitalize()
country   = data["sys"]["country"]

# Print nicely
print(f"\n📍 {city.capitalize()}, {country}")
print(f"🌡  Temperature : {temp}°C")
print(f"💧  Humidity    : {humidity}%")
print(f"🌬  Wind        : {wind} km/h")
print(f"☁   Condition   : {condition}\n")