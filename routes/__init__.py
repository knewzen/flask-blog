from flask import Blueprint
from flask_login import LoginManager
from app.controllers import *




Route = Blueprint('route',__name__,template_folder="../public/views", static_folder="../public/assets")
login_manager = LoginManager()