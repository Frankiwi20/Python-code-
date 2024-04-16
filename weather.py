import requests


class WeatherData:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'  # Request temperature in Celsius
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raise exception for non-200 status codes

            data = response.json()
            description = data['weather'][0]['description']
            temperature_celsius = data['main']['temp']
            temperature_fahrenheit = (temperature_celsius * 9 / 5) + 32

            return f"Weather in {city.title()}: {description}, Temperature: {temperature_celsius:.2f} °C ({temperature_fahrenheit:.2f} °F)"

        except requests.RequestException as e:
            return f"Failed to retrieve weather data: {e}"# request failed error, related to http requests

        except (KeyError, IndexError) as e:
            return f"Error parsing weather data: {e}" # exception when parsing wheather data in json file

        except Exception as e:
            return f"An unexpected error occurred: {e}"# handling any other expected error


# Example usage:
weather_instance = WeatherData('87596aa1a39a1925e6cf81e1c866d9ec')
city_name = 'New York'
weather_info = weather_instance.get_weather(city_name)
print(weather_info)
