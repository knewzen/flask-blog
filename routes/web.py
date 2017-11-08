from . import Route, login_manager
from flask import request
from app.controllers.HomeController import HomeController 
from app.controllers.AuthController import AuthController
from flask_login import LoginManager, login_required , login_user
from app.models.User import User

# declare controller
home = HomeController()
auth = AuthController()
login_manager = LoginManager()
user = User()


@login_manager.user_loader
def load_loader(user_id):
    return User.get(user_id)

@Route.route('/')
def index(): 
     return home.index()

@Route.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return auth.login()
    elif request.method == 'POST':
        return auth.login_check()

@Route.route('/register', methods=['GET','POST'])
def register():
    
    if request.method == 'GET':
        return auth.register()

    elif request.method == 'POST':
        return auth.register_check()


@Route.route('/admin')
@login_required
def admin():
    return "ini admin"        


    