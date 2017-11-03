from . import Route
from app.controllers.HomeController import HomeController 
from app.controllers.AuthController import AuthController 

# declare controller
home = HomeController()
auth = AuthController()


@Route.route('/')
def index(): 
    return home.index()

@Route.route('/login')
def login():
    return auth.login()

    