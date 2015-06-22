from flask import Flask
from flask_peewee.db import Database
from flask.ext.security import (
    Security, 
    PeeweeUserDatastore, 
    UserMixin, 
    RoleMixin,
)
from peewee import *


# Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['DATABASE'] = {
    'name': 'example.db',
    'engine': 'peewee.SqliteDatabase',
}

# Create database connection object
db = Database(app)



# Setup Flask-Security
from app.models import User, Role, UserRoles
user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
security = Security(app, user_datastore)

from app.admin.views import admin
app.register_blueprint(admin)