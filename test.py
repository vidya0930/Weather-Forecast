import http.client
import json

city_name = input("kathmandu:")

conn = http.client.HTTPSConnection("open-weather13.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "2eeb97dbcbmsh0c8fdc1f20d6a6cp1eb6f1jsnee46e7f4aff2",
    'x-rapidapi-host': "open-weather13.p.rapidapi.com"
}

conn.request("GET", "/city/kathmandu/EN", headers=headers)

res = conn.getresponse()
data = res.read()

# Parse the JSON response
response_json = json.loads(data.decode("utf-8"))

# Extract weather data
city = response_json.get('name', 'N/A')
country = response_json.get('sys', {}).get('country', 'N/A')
weather_description = response_json.get('weather', [{}])[0].get('description', 'N/A')
temperature = response_json.get('main', {}).get('temp', 'N/A')
feels_like = response_json.get('main', {}).get('feels_like', 'N/A')
humidity = response_json.get('main', {}).get('humidity', 'N/A')
pressure = response_json.get('main', {}).get('pressure', 'N/A')
wind_speed = response_json.get('wind', {}).get('speed', 'N/A')
visibility = response_json.get('visibility', 'N/A')

# Print the output in a more readable format
print(f"Weather data for {city}, {country}:")
print(f"Weather: {weather_description.capitalize()}")
print(f"Temperature: {temperature}°C")
print(f"Feels Like: {feels_like}°C")
print(f"Humidity: {humidity}%")
print(f"Pressure: {pressure} hPa")
print(f"Wind Speed: {wind_speed} m/s")
print(f"Visibility: {visibility} meters")
