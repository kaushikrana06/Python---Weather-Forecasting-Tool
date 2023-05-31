import requests
import json
import argparse

def get_weather(city):
    # Enter your OpenWeatherMap API key here
    api_key = "574e1b44b52d5fe65d508b4e754ec754"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Send a GET request to the OpenWeatherMap API
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        # Parse the JSON response
        data = json.loads(response.text)
        
        # Extract relevant weather information
        weather = data["weather"][0]["main"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        # Display the weather forecast
        print(f"Weather forecast for {city}:")
        print(f"Condition: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Error occurred while fetching weather data.")

def main():
    parser = argparse.ArgumentParser(description="Get the current weather forecast for a city.")
    parser.add_argument("city", help="Name of the city")
    args = parser.parse_args()
    
    get_weather(args.city)

if __name__ == "__main__":
    main()
