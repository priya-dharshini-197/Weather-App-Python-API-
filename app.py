from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    city = request.args.get("city")

    if city:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)
        data = response.json()

        temp = data["current_condition"][0]["temp_C"]
        condition = data["current_condition"][0]["weatherDesc"][0]["value"]
        humidity = data["current_condition"][0]["humidity"]
        wind = data["current_condition"][0]["windspeedKmph"]
        feels_like = data["current_condition"][0]["FeelsLikeC"]
    else:
        temp = "N/A"
        condition = "N/A"
        humidity = "N/A"
        wind = "N/A"
        feels_like = "N/A"

    return render_template(
        "index.html",
        city=city,
        temp=temp,
        condition=condition,
        humidity=humidity,
        wind=wind,
        feels_like=feels_like
    )

if __name__ == "__main__":
    app.run(debug=True)
