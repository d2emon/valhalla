from flask import Flask, render_template
from flask_script import Manager
# from flask_bootstrap import Bootstrap
# from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand


from config import app_config


import os


import logging
from logging.handlers import RotatingFileHandler


db = SQLAlchemy()
# login_manager = LoginManager()


def create_logger(log_config=dict()):
    handler = RotatingFileHandler(
        log_config.get("FILENAME", "logfile.log"),
        maxBytes=log_config.get("MAX_BYTES", 1024 * 1024),
        backupCount=log_config.get("BACKUP_COUNT", 0),
    )
    formatter = logging.Formatter(log_config.get("FORMAT"))
    handler.setFormatter(formatter)
    return handler


def create_app(config_name='production'):
    app = Flask(__name__, instance_relative_config=True)
    print("Loading \"%s\" config..." % (config_name))
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # Setting up templates and static
    # app.template_folder = app.config.get('TEMPLATE_FOLDER', '')
    # app.static_folder = app.config.get('STATIC_FOLDER', '')

    log_config = app.config.get("LOG", dict())
    app.logger.addHandler(create_logger(log_config))
    app.logger.debug("Config: %s" % (app.config))

    db.init_app(app)

    # session = Session(app)
    # bootstrap = Bootstrap(app)
    # login_manager.init_app(app)
    # login_manager.login_message = "You must be logged in to access this page."
    # login_manager.login_view = "auth.login"
    migrate = Migrate(app, db)

    from story import models

    # Installing blueprints
    from blueprints.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from blueprints.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    # Customizing errors
    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Server Error'), 500

    return app


# from execom.commands import *
# from execom.views import *
# from case.views import *


config_name = os.getenv('FLASK_CONFIG', 'production')
app = create_app(config_name)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    app.run()
