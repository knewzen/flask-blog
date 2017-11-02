from flask import Blueprint
from app.controllers import *




Route = Blueprint('route',__name__,template_folder="../public/views", static_folder="../public")
