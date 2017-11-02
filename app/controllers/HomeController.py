from flask import render_template

class HomeController(object):

    def index(self):
        return render_template("home/index.html")