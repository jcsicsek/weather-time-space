from flask import Flask
from flask import jsonify
import requests
import os

app = Flask(__name__)

@app.route("/")
def hello():
  darkskyKey = os.environ['DARKSKY_KEY'];
  weatherData = requests.get(f"https://api.darksky.net/forecast/{darkskyKey}/37.8267,-122.4233")
  return jsonify(weatherData.json())

if __name__ == "__main__":
  app.run()
