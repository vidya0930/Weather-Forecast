import tkinter as tk
from tkinter import messagebox
import requests

def get_coordinates(city_name, api_key):
    """Fetch latitude and longitude of a city using OpenWeatherMap Geocoding API."""
    geocode_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": city_name,
        "limit": 1,
        "appid": api_key
    }
    try:
        response = requests.get(geocode_url, params=params)
        response.raise_for_status()
        data = response.json()

        if len(data) > 0:
            lat = data[0]["lat"]
            lon = data[0]["lon"]
            return lat, lon
        else:
            messagebox.showerror("Error", "City not found. Please check the city name.")
            return None, None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching coordinates: {e}")
        return None, None

def get_weather(lat, lon, api_key):
    """Fetch weather data using OpenWeatherMap Current Weather API."""
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(weather_url, params=params)
        response.raise_for_status()
        data = response.json()

        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        return city, country, temp, weather_desc, humidity, wind_speed
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching weather data: {e}")
        return None

def show_weather():
    """Handles user input and displays weather data."""
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    lat, lon = get_coordinates(city, API_KEY)
    if lat and lon:
        weather_data = get_weather(lat, lon, API_KEY)
        if weather_data:
            city, country, temp, weather_desc, humidity, wind_speed = weather_data

            # Update labels with weather information
            city_label.config(text=f"{city}, {country}")
            temp_label.config(text=f"Temperature: {temp}°C")
            weather_label.config(text=f"Condition: {weather_desc}")
            humidity_label.config(text=f"Humidity: {humidity}%")
            wind_label.config(text=f"Wind Speed: {wind_speed} m/s")

# Your OpenWeatherMap API key
API_KEY = "784e79cba2b1e446d5eb154efc6db645"

# Tkinter GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.config(bg="#f0f8ff")  # Light blue background

# Title label
title_label = tk.Label(root, text="Weather App", font=("Helvetica", 24, "bold"), bg="#f0f8ff")
title_label.pack(pady=20)

# City input
city_entry_label = tk.Label(root, text="Enter City:", font=("Helvetica", 14), bg="#f0f8ff")
city_entry_label.pack(pady=5)
city_entry = tk.Entry(root, font=("Helvetica", 14), width=25, borderwidth=2, relief="solid")
city_entry.pack(pady=10)

# Search button
search_button = tk.Button(root, text="Get Weather", font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white", command=show_weather)
search_button.pack(pady=10)

# Weather information labels
city_label = tk.Label(root, text="City, Country", font=("Helvetica", 18), bg="#f0f8ff")
city_label.pack(pady=5)

temp_label = tk.Label(root, text="Temperature: 0°C", font=("Helvetica", 14), bg="#f0f8ff")
temp_label.pack(pady=5)

weather_label = tk.Label(root, text="Condition: Clear sky", font=("Helvetica", 14), bg="#f0f8ff")
weather_label.pack(pady=5)

humidity_label = tk.Label(root, text="Humidity: 0%", font=("Helvetica", 14), bg="#f0f8ff")
humidity_label.pack(pady=5)

wind_label = tk.Label(root, text="Wind Speed: 0 m/s", font=("Helvetica", 14), bg="#f0f8ff")
wind_label.pack(pady=5)

# Run the app
root.mainloop()
