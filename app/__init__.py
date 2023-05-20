# Application entry point
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from app.data.database import verify_cliente_is_populated, populate_database
from app import models
from app.models.rdb import db


# Globally accessible libraries
ma = Marshmallow()

# Application Factory App
def create_app() -> Flask:
    """Create an app by initializing components"""
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    ma.init_app(app)
    CORS(app) # This will enable CORS for all routes

    with app.app_context():
        db.create_all()  

        if verify_cliente_is_populated(db):
            populate_database(db)

        # Include our Routes in our context
        from app.routes import cliente, fake_lead

        # Register Blueprints
        app.register_blueprint(cliente)
        app.register_blueprint(fake_lead)
        return app
