import requests
from weather_data import Country, City 

def fetch_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use metric units for temperature
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(api_key, country):
    for city in country.cities:
        weather_data = fetch_weather(api_key, city.name)
        if weather_data:
            print(f"Weather in {city.name}, {country.name}:")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Weather: {weather_data['weather'][0]['description']}\n")
        else:
            print(f"Failed to fetch weather data for {city.name}\n")

def main():
    api_key = "47301f56a67e3d661899252bc5c7af0b"

    philippines= Country(name="The Philippines")
    cebu = City(name="Cebu City", country=philippines)
    lapu_lapu = City(name="Lapu-Lapu City", country=philippines)
    
    philippines.add_city(cebu)
    philippines.add_city(lapu_lapu)

    display_weather(api_key, philippines)

if __name__ == "__main__":
    main()

