03/25/2026 
- Completed a simple Python script that gathers system information to better understand the working environment in WSL.

03/31/2026 
- Started a weather API script using 'openweathermap.org'. 
- Sent GET requests with lat/lon parameters and parsed JSON response. 
- Extracted key fields (city, weather, description, temperature), formatted strings (title case, Fahrenheit), and saved structured output to a JSON file.

04/02/2026 
- Added an api_key.py file so that it can store my API from openweathermap.org.

04/10/2026
- Added a daily run check using Task Scheduler. 
- Implemented a function to prevent the script from running multiple times per day. 
- Also ensured that previously parsed data is preserved instead of overwriting weather_data.json.