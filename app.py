from flask import Flask, jsonify, request

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# Simple city-to-weather map
CITY_WEATHER = {
    "Berlin": {"temperature": 15, "humidity": 70, "condition": "Cloudy"},
    "London": {"temperature": 12, "humidity": 80, "condition": "Rainy"},
    "Paris": {"temperature": 18, "humidity": 65, "condition": "Sunny"},
    "Dhaka": {"temperature": 28, "humidity": 75, "condition": "Humid"},
}

@app.route("/weather")
def get_weather():
    city = request.args.get("city")
    if not city or city not in CITY_WEATHER:
        return jsonify({"error": "City not found"}), 404
    return jsonify(CITY_WEATHER[city])

if __name__ == "__main__":
    app.run(debug=True)
