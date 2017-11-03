from . import Route
from flask import request
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

@Route.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return auth.register()

    elif request.method == 'POST':
        return auth.register_check()


    