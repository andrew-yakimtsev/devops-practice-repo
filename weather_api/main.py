import requests, json
from datetime import datetime
from api_key import api

today = datetime.now()
formatted_date = today.strftime("%Y-%m-%d")

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
    file_path = 'weather_api/weather_data.json'

    with open(file_path, 'w') as json_file:
        json.dump(api_call(), json_file, indent=4)

print_json()

#! TODO: Don't Override Parse, Add "Run on startup (CRON)"