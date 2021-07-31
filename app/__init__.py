from flask import Flask

from app.config import config_by_name
from app.error import *
from app.extensions import db, ma
from app.routes.index import index
from app.routes.people import people


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    ma.init_app(app)
    app.register_blueprint(index)
    app.register_blueprint(people, url_prefix='/people')
    app.register_error_handler(400, handle_bad_request)
    app.register_error_handler(404, handle_invalid_route)
    app.register_error_handler(405, handle_invalid_method)
    app.register_error_handler(Exception, handle_generic_exception)
    app.register_error_handler(ValidationError, handle_validation_error)
    app.register_error_handler(ResourceNotFoundError, handle_not_found_error)
    return app
