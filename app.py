"""
PROJECT:        Basic Weather App
FILENAME:       app.py
AUTHOR:         Aakash Sudhakar
DESCRIPTION:    Basic take home project for SPD 1.02. Construct
                a functional weather app with good code practices.
"""

############################################################
################ IMPORTS AND INITIALIZATIONS ###############
############################################################


from flask import Flask, render_template
import requests as req
import json

app = Flask(__name__)


############################################################
######################## APP ROUTING #######################
############################################################


@app.route("/")
def get_index():
    # Instantiate Weather App Template
    PATH_INDEX = "index.html"

    # Instantiate Weather API Location
    URL = "https://api.openweathermap.org/data/2.5/weather?lat=37.7749&lon=122.4194&units=metric&APPID=a4f15e7f800810b40af6bbc478d3e9c5"

    # Convert Weather Call to Parseable JSON Object
    parseable = req.get(URL).content
    data = json.loads(parseable)

    # Extract and Return Data from Parsed Weather JSON Object
    weather_all = data["weather"]
    weather_main, weather_desc = weather_all[0]["main"], weather_all[0]["description"]
    return render_template(PATH_INDEX, weather=weather_main, description=weather_desc)


############################################################
######################## APP ROUTING #######################
############################################################


if __name__ == "__main__":
    hostname, portname = "0.0.0.0", "8080"
    app.run(host=hostname, port=portname, debug=True)