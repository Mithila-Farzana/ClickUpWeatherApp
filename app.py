from flask import Flask, render_template, request, jsonify
from weather_client import WeatherAPIClient

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/weather", methods=["POST"])
def weather():
    city = request.form.get("city")
    client = WeatherAPIClient()          
    data = client.get_weather(city)      

    current = data["current_condition"][0]

    return jsonify({
        "temp": current["temp_C"],
        "feels": current["FeelsLikeC"],
        "condition": current["weatherDesc"][0]["value"],
        "humidity": current["humidity"]
    })

if __name__ == "__main__":
    app.run(debug=True)
