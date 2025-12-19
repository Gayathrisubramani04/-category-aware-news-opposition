from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    from .api.health import bp as health_bp
    app.register_blueprint(health_bp)

    # Phase 2 service blueprints
    from .api.category import bp as category_bp
    from .api.sentiment import bp as sentiment_bp
    from .api.opposition import bp as opposition_bp
    from .api.analyze import bp as analyze_bp

    app.register_blueprint(category_bp)
    app.register_blueprint(sentiment_bp)
    app.register_blueprint(opposition_bp)
    app.register_blueprint(analyze_bp)

    return app
