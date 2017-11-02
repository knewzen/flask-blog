from . import Route
from app.controllers.HomeController import HomeController 

@Route.route('/')
def index():
    home = HomeController()
    return home.index()

    