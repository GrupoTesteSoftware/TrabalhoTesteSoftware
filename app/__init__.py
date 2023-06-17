# Application entry point
from flask import Flask, render_template, send_from_directory
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from app.data.database import verify_cliente_is_populated, populate_database
from app import models
from app.models.rdb import db
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_restx import Api,Resource

# Globally accessible libraries
ma = Marshmallow()

# Application Factory App
def create_app() -> Flask:
    """Create an app by initializing components"""
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_object('config.Config')
    
    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route('/swagger/<path:path>')
    def send_swagger_static(path):
        return send_from_directory('swagger', path)
    
    # Initialize database and marshmallow
    db.init_app(app)
    ma.init_app(app)
    
    # Enable CORS for all routes
    CORS(app)
    
    with app.app_context():
        db.create_all()  

        if verify_cliente_is_populated(db):
            populate_database(db)

        # Include our Routes in our context
        from app.routes import cliente, Produto, enderecoscliente

        # Register Blueprints
        app.register_blueprint(cliente)
        app.register_blueprint(Produto)
        app.register_blueprint(enderecoscliente)
        
        # Create Swagger API documentation
        api = Api(app, version='1.0', title='Your API', description='API documentation',doc="/swagger")
        @api.route('/hello')
        class HelloResource(Resource):
            def get(self):
                    """An example endpoint that returns a greeting."""
                    return "Hello, World!Te"
        return app
    
app = create_app()