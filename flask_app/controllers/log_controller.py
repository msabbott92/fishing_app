from flask import render_template, request, redirect, session, flash
import requests
from flask_app import app
from flask_cors import CORS
from flask_bcrypt import Bcrypt  
from flask_app.models.user_model import User
from flask_app.models.log_model import Logs

API_KEY = '80ba011a0bb34c597f31f439084f2bd2'

@app.route("/dashboard")
def dashboard():
    show_modal = session.pop('show_modal', False)

    data = {
        "id": session["user_id"]
    }
    return render_template("dashboard.html",user = User.get_one_by_id(data), logs = Logs.get_all_logs_by_user(data), show_modal=show_modal)

@app.route('/weather')
def get_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    api_url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}'

    response = requests.get(api_url)
    weather_data = response.json()

    return weather_data

@app.route('/new/log', methods=['POST'])
def new_log():
    if 'user_id' not in session:
        return redirect("/")
    if not Logs.validate_log(request.form):
        flash ("Please fill out log form again")
        return redirect("/dashboard")
    data = {
        "date" : request.form["date"],
        "location": request.form["location"],
        "body_water": request.form["body_water"],
        "temp": request.form["temp"],
        "fish_caught": request.form["fish_caught"],
        "fish_type": request.form["fish_type"],
        "flies_used": request.form["flies_used"],
        "comments": request.form["comments"], 
        "user_id": session["user_id"]
    }
    print(data)
    Logs.save(data)
    return redirect('/dashboard')

@app.route("/log/show/<int:id>")
def view_log(id):
    if 'user_id' not in session:
        return redirect("/")
    return render_template("view_log.html", log = Logs.get_log_by_id({"id":id}))

@app.route("/log/edit/<int:id>")
def edit_log(id):
    if 'user_id' not in session:
        return redirect("/") 
    return render_template("edit_log.html", log = Logs.get_log_by_id({"id":id}))

@app.route("/log/update/<int:id>", methods = ['POST'])
def update_log(id):
    if 'user_id' not in session:
        return redirect("/")
    if not Logs.validate_log(request.form):
        return redirect(f"/log/edit/{id}")
    data = {
        "id": id,
        "date" : request.form["date"],
        "location": request.form["location"],
        "body_water": request.form["body_water"],
        "temp": request.form["temp"],
        "fish_caught": request.form["fish_caught"],
        "fish_type": request.form["fish_type"],
        "flies_used": request.form["flies_used"],
        "comments": request.form["comments"],
        "user_id": session["user_id"]
    }
    print("made it here")
    Logs.update(data)
    return redirect('/dashboard')

@app.route("/delete/log/<int:id>")
def delete_log(id):
    if 'user_id' not in session:
        return redirect('/')
    Logs.delete_log({'id':id})
    return redirect("/dashboard")

