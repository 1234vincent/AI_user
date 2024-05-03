# AI_user/__init__.py
from flask import Flask
from AI_user.models.user import db
from AI_user.url.user import user_bp  

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:0111284Tony!@localhost:3306/User_test'
    db.init_app(app)
    app.register_blueprint(user_bp)

    return app
