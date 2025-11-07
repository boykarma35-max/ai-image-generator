from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from backend.config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    with app.app_context():
        from backend.models import User
        db.create_all()
    
    @app.route('/')
    def index():
        return 'Welcome to AI Image Generator!'
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
