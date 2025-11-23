import requests

# Singleton Pattern
class WeatherAPIClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WeatherAPIClient, cls).__new__(cls)
        return cls._instance

    # Facade Method 
    def get_weather(self, city):
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)
        return response.json()
