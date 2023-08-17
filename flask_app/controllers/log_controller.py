from flask import render_template, request, redirect, session, flash
import requests
from flask_app import app
from flask_cors import CORS
from flask_bcrypt import Bcrypt  
from flask_app.models.user_model import User

API_KEY = '80ba011a0bb34c597f31f439084f2bd2'

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route('/weather')
def get_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    api_url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}'

    response = requests.get(api_url)
    weather_data = response.json()

    return weather_data

