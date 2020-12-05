from flask import Flask

from database import db, ma
from products.views import products


def create_app(config_file='settings.py'):
    application = Flask(__name__)
    application.config.from_pyfile(config_file)
    db.init_app(application)
    with application.app_context():
        db.create_all()
    ma.init_app(application)
    application.register_blueprint(products, url_prefix='/product')
    return application


if __name__ == '__main__':
    app = create_app()
    app.run(debug=False, port=4000)
