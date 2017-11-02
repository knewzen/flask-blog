from flask import Flask
from routes.web import Route

app = Flask(__name__)
app.register_blueprint(Route)

app.run(debug=True)