from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
from routes.uploads import upload
from model import db
from model import Event

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4donald5@localhost/baby-tracker'
db = SQLAlchemy(app)
CORS(app)

app.register_blueprint(upload, url_prefix="")



if __name__ == '__main__':
    app.run()