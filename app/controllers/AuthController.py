from flask import render_template
from app.models.User import User

class AuthController(object):


    def login(self):

        users = User()
        usr = users.query.all()

        return render_template('auth/login/index.html', users=usr)