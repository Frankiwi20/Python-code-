import requests
import csv
class Data:
    def fetch_weather_data(city):
        API_KEY = '87596aa1a39a1925e6cf81e1c866d9ec' \
                  ''
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        url = f"{BASE_URL}appid={API_KEY}&q={city}"
        response = requests.get(url)
        return response.json()

    def process_weather_data(weather_data):
        if weather_data.get("cod") != 200:
            return {}

        processed_data = {
            "city": weather_data.get("name"),
            "temperature": weather_data.get("main", {}).get("temp"),
            "humidity": weather_data.get("main", {}).get("humidity"),
            "description": weather_data.get("weather", [{}])[0].get("description")
        }
        return processed_data


    def write_data_to_csv(data, filename="weather_data.csv"):
        fieldnames = ['city', 'temperature', 'humidity', 'description']

        # Check if file exists to determine if headers need to be written
        try:
            with open(filename, 'x', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(data)
        except FileExistsError:
            with open(filename, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(data)

