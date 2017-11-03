from flask import Flask
from routes.web import Route
from config.database import db
from env import *
from flask_session import Session

app = Flask(__name__)
sess = Session()
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'reds209ndsldssdsljdsldsdsljdsldksdksdsdfsfsfsfis'
app.register_blueprint(Route)

try:
    app.config['SQLALCHEMY_DATABASE_URI'] = "%s://%s:%s@%s/%s" % (DB_ENGINE,DB_USERNAME,DB_PASSWORD,DB_HOST,DB_NAME)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)  
    sess.init_app(app)  
except ValueError as e:
    print(e)

app.run(debug=True)