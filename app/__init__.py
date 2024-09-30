from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """
    Create and configure an instance of the Flask application.

    This function initializes a new Flask app, sets up the configuration,
    initializes the database and migration objects, and imports the
    routes and models.

    Returns:
        Flask: A configured Flask application instance ready to serve requests.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app import routes, models
    return app