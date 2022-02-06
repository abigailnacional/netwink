from flask import Flask
from flask_login import LoginManager
#from flask_babel import Babel
#from flask_babel import _, lazy_gettext as _l

def create_bps(app):
    from .index import bp as index_bp
    app.register_blueprint(index_bp)

    from .users import bp as user_bp
    app.register_blueprint(user_bp)

    import sys
    sys.path.append('webappdb')
    from create import bp as create_bp
    app.register_blueprint(create_bp)

    return app
    