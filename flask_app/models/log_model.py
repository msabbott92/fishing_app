from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
from flask_app.models.user_model import User

class Logs:
    db = "fishing_app"
    def __init__(self, data):
        self.id = data["id"]
        self.date = data["date"]
        self.location = data["location"]
        self.body_water = data["body_water"]
        self.temp = data["temp"]
        self.fish_caught = data["fish_caught"]
        self.fish_type = data["fish_type"]
        self.flies_used = data["flies_used"]
        self.comments = data["comments"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data["user_id"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO log (date, location, body_water, temp, fish_caught, fish_type, flies_used, comments, created_at, updated_at, user_id) VALUES (%(date)s, %(location)s, %(body_water)s, %(temp)s, %(fish_caught)s, %(fish_type)s, %(flies_used)s, %(comments)s, NOW(), NOW(), %(user_id)s);"
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)
        return results
    
    @staticmethod
    def validate_log(data):
        is_valid = True
        if  data['date'] == "":
            flash("Please list valid date")
            is_valid = False
        if len(data['location']) < 3:
            flash("Please list valid location")
            is_valid = False
        if len(data['body_water']) < 2:
            flash("Please list valid body of water")
            is_valid = False
        if len(data['temp']) < 1:
            flash("Please list valid temperature")
            is_valid = False
        if len(data['fish_type']) < 2:
            flash("Please list valid fish type")
            is_valid = False
        if len(data['flies_used']) < 2:
            flash("Please list valid flies used")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_all_logs(cls):
        query = "SELECT * FROM log LEFT JOIN users on log.user_id = users.id"
        results = connectToMySQL(cls.db).query_db(query)
        all_logs = []
        for row in results:
            log_by_user = cls(row)
            user_info = {
                "id":row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"]
            }
            log_by_user.user = User(user_info)
            all_logs.append(log_by_user)
        return all_logs
    
    @classmethod
    def get_log_by_id(cls, data):
        query = "SELECT * FROM log LEFT JOIN users on log.user_id = users.id WHERE log.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def get_all_logs_by_user(cls, data):
        query = "SELECT * FROM log LEFT JOIN users on log.user_id = users.id WHERE log.user_id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        all_logs = []
        for row in results:
            log_by_user = cls(row)
            user_info = {
                "id":row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"]
            }
            log_by_user.user = User(user_info)
            all_logs.append(log_by_user)
        return all_logs
    
    @classmethod
    def update(cls, data):
        print("got to model")
        query = "UPDATE log SET date = %(date)s, location = %(location)s, body_water = %(body_water)s, temp = %(temp)s, fish_caught = %(fish_caught)s, fish_type = %(fish_type)s, flies_used = %(flies_used)s, comments = %(comments)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete_log(cls, data):
        query = "DELETE FROM log WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    

    
    