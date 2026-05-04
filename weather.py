from database import init_db, save_search, get_history
import requests
import sys
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
init_db()

API_KEY = os.getenv("API_KEY")

# 👉 HISTORY MODE (run BEFORE API call)
if len(sys.argv) > 1 and sys.argv[1] == "--history":
    print("\n📋 Last 5 searches:\n")
    rows = get_history()
    if not rows:
        print("No searches yet.")
    else:
        for row in rows:
            print(f"  {row[3]} — {row[0]}, {row[1]} | {row[2]}°C | {row[4]}")
    sys.exit()

# Get city from terminal
city = sys.argv[1] if len(sys.argv) > 1 else "Chennai"

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# API call
response = requests.get(url)
data = response.json()

# Error handling
if data.get("cod") != 200:
    print(f"City '{city}' not found. Try again.")
    sys.exit()

# Extract values
temp      = data["main"]["temp"]
humidity  = data["main"]["humidity"]
wind      = data["wind"]["speed"]
condition = data["weather"][0]["description"].capitalize()
country   = data["sys"]["country"]

# Display output
print(f"\n📍 {city.capitalize()}, {country}")
print(f"🌡  Temperature : {temp}°C")
print(f"💧  Humidity    : {humidity}%")
print(f"🌬  Wind        : {wind} km/h")
print(f"☁   Condition   : {condition}\n")

# 👉 SAVE TO DATABASE
save_search(city, country, temp, humidity, condition)