from flask import Flask, request
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
from routes.uploads import upload
from model import db
from model import Upload
# from model import Event

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4donald5@localhost/baby-tracker'
    app.config["SECRET_KEY"] = '5f352379324c22463451387a0aec5d2f'
    # db = SQLAlchemy(app)

    CORS(app)
    db.init_app(app)
    app.register_blueprint(upload, url_prefix="")
    with app.app_context():
        db.create_all()

    if __name__ == '__main__':
        app.run(debug=True)
    
    return app


# app.register_blueprint(upload, url_prefix="")

# with app.app_context():
#     db.create_all()

# if __name__ == '__main__':
#     app.run(debug=True)