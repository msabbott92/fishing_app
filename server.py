from flask_app import app
from flask_app.controllers import user_controller
from flask_app.controllers import log_controller
from flask_app.models.user_model import User
from flask_app.models.log_model import Logs


if __name__ == "__main__":
    app.run(debug=True)