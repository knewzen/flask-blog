from . import Route
from app.controllers.HomeController import HomeController 

# declare controller
home = HomeController()


@Route.route('/')
def index():
    
    return home.index()

    