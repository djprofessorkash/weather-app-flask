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
import requests, json

app = Flask(__name__)


############################################################
######################## APP ROUTING #######################
############################################################


@app.route("/")
def get_index():
    pass


############################################################
######################## APP ROUTING #######################
############################################################


if __name__ == "__main__":
    HOSTNAME, PORTNAME = "0.0.0.0", "8080"
    app.run(host=HOSTNAME, port=PORTNAME, debug=True)