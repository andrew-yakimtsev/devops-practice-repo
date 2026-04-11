import requests, json
from pathlib import Path
from datetime import datetime
from api_key import api

BASE_DIR = Path(__file__).resolve().parent
weather_file = BASE_DIR / "weather_data.jsonl"
last_run_file = BASE_DIR / "last_run.txt"

today = datetime.now().strftime("%Y-%m-%d")

def already_ran_today():
    if last_run_file.exists():
        last_run = last_run_file.read_text().strip()
        return last_run == today
    return False

def mark_ran_today():
    last_run_file.write_text(today)

def api_call():
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "lat": 38.5816,
        "lon": -121.4944,
        "appid": api,
        "units": "imperial"
    }

    response = requests.get(url, params=params)
    data = response.json()

    parsed_data = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "name": data["name"].title(),
        "weather": data["weather"][0]["main"].title(),
        "description": data["weather"][0]["description"].title(),
        "temp": f"{data['main']['temp']}F"
    }

    print(f"Data successfully parsed!")
    return parsed_data

def print_json():
    with open(weather_file, 'a') as json_file:
        json.dump(api_call(), json_file, indent=4)
        json_file.write("\n")

if already_ran_today():
    print("Already ran today. Exiting...")
else:
    print_json()
    mark_ran_today()