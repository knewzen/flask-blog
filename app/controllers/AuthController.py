from flask import render_template

class AuthController(object):


    def login(self):
        return render_template('auth/login/index.html')