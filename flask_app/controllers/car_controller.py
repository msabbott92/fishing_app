from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt  
from flask_app.models.user_model import User
from flask_app.models.car_model import Cars


@app.route("/dashboard")
def dashboard():
    data = {
        "id": session["user_id"]
    }

    return render_template("dashboard.html", user = User.get_one_by_id(data), cars = Cars.get_all_cars_sale())

@app.route("/new")
def new_car_sale():
    if 'user_id' not in session:
        return redirect("/")
    return render_template("new_car.html")

@app.route("/new/car_listed", methods=['POST'])
def list_new_car():
    if 'user_id' not in session:
        return redirect("/")
    if not Cars.validate_car(request.form):
        return redirect("/new")
    data = {
        "price" : request.form["price"],
        "model": request.form["model"],
        "make": request.form["make"],
        "year": request.form["year"],
        "description": request.form["description"],
        "user_id": session["user_id"]
    }
    Cars.save(data)
    return redirect('/dashboard')

@app.route("/car/show/<int:id>")
def view_car(id):
    if 'user_id' not in session:
        return redirect("/")
    return render_template("view_car.html", car = Cars.get_car_by_id({"id":id}))

@app.route("/car/edit/<int:id>")
def edit_car(id):
    if 'user_id' not in session:
        return redirect("/") 
    return render_template("edit_car.html", car = Cars.get_car_by_id({"id":id}))

@app.route("/car/update/<int:id>", methods = ['POST'])
def update_car(id):
    if 'user_id' not in session:
        return redirect("/")
    if not Cars.validate_car(request.form):
        return redirect(f"/car/edit/{id}")
    data = {
        "id": id,
        "price" : request.form["price"],
        "model": request.form["model"],
        "make": request.form["make"],
        "year": request.form["year"],
        "description": request.form["description"],
    }
    Cars.update_car(data)
    return redirect("/dashboard")

@app.route("/delete/car/<int:id>")
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    Cars.delete_car({'id':id})
    return redirect("/dashboard")

@app.route("/purchase/<int:id>")
def purchase_car(id):
    data = {
        "id": id,
        "buyer_id": session['user_id'],
        }
    print(data)
    
    Cars.purchase(data)
    return redirect("/dashboard")

@app.route("/purchases/")
def view_purchases():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    return render_template("purchases.html", user = User.get_one_by_id(data), cars = Cars.get_purchases_by_user(data))