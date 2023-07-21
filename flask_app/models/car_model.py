from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user_model import User

class Cars:
    db = "car_dealz_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.price = data["price"]
        self.model = data["model"]
        self.make = data["make"]
        self.year = data["year"]
        self.description = data["description"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data["user_id"]
        self.seller = None
        self.buyer = None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO cars (price, model, make, year, description, created_at, updated_at, user_id) VALUES (%(price)s, %(model)s, %(make)s, %(year)s, %(description)s, NOW(), NOW(), %(user_id)s);"
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)
        return results

    @staticmethod
    def validate_car(data):
        is_valid = True

        if  data['price'] == "":
            flash("Name must be at least 3 characters long")
            is_valid = False
        if len(data['model']) < 2:
            flash("Please list valid Model")
            is_valid = False
        if len(data['make']) < 2:
            flash("Please list valid Make")
            is_valid = False
        if "year" not in data:
            flash("Please put car's year")
            is_valid = False
        if len(data["description"]) < 10:
            flash("Please provide valid description")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_all_cars_sale(cls):
        query = "SELECT * FROM cars LEFT JOIN users on cars.user_id = users.id"
        results = connectToMySQL(cls.db).query_db(query)
        all_cars = []
        for row in results:
            car_by_seller = cls(row)
            if row["buyer_id"] is not None: 
                car_by_seller.buyer = "SOLD"
            seller_info = {
                "id":row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
            }
            car_by_seller.seller = seller_info
            all_cars.append(car_by_seller)
        return all_cars
    
    @classmethod
    def get_car_by_id(cls, data):
        print(data)
        query = "SELECT * FROM cars JOIN users on cars.user_id = users.id WHERE cars.id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        car_data = results[0]
        car_by_id = cls(car_data)
        user_info = {
                "id":car_data["users.id"],
                "first_name": car_data["first_name"],
                "last_name": car_data["last_name"],
            }
        car_by_id.seller = user_info
        return car_by_id
    
    @classmethod
    def update_car(cls, data):
        query = " UPDATE cars SET price = %(price)s, model = %(model)s, make = %(make)s, year = %(year)s, description = %(description)s WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete_car(cls, data):
        query = "DELETE FROM cars WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def purchase(cls, data):
        update_query = "UPDATE cars SET buyer_id = %(buyer_id)s WHERE id = %(id)s"
        connectToMySQL(cls.db).query_db(update_query, data)
    
        insert_query = "INSERT INTO purchases (car_id, user_id, created_at, updated_at) VALUES (%(id)s, %(buyer_id)s, NOW(), NOW())"
        return connectToMySQL(cls.db).query_db(insert_query, data)
    
    @classmethod
    def get_purchases_by_user(cls, data):
        query = "SELECT * FROM purchases JOIN users ON purchases.user_id = users.id JOIN cars ON purchases.car_id = cars.id WHERE users.id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results:
            return None
        cars_purchased = []
        for result in results:
            car = cls(result)
            buyer_info = {
                    "id":result["users.id"],
                    "first_name": result["first_name"],
                    "last_name": result["last_name"],
                }
            car.buyer = buyer_info
            cars_purchased.append(car)
        
        return cars_purchased
    
        
    
    