import requests

class WeatherAPIClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WeatherAPIClient, cls).__new__(cls)
        return cls._instance

    def get_weather(self, city):
        url = "http://127.0.0.1:5000/weather"
        params = {"city": city}
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise ValueError(f"Error fetching weather for {city}")
        return response.json()

# Example usage
client = WeatherAPIClient()
weather = client.get_weather("Berlin")
print(weather)
