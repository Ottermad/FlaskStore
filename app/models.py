from app import db
from peewee import *
from flask.ext.security import (
    UserMixin, 
    RoleMixin,
)


class Role(db.Model, RoleMixin):
    name = CharField(unique=True)
    description = TextField(null=True)

class User(db.Model, UserMixin):
    email = TextField()
    password = TextField()
    active = BooleanField(default=True)
    confirmed_at = DateTimeField(null=True)

class UserRoles(db.Model):
    # Because peewee does not come with built-in many-to-many
    # relationships, we need this intermediary class to link
    # user to roles.
    user = ForeignKeyField(User, related_name='roles')
    role = ForeignKeyField(Role, related_name='users')
    name = property(lambda self: self.role.name)
    description = property(lambda self: self.role.description)
    
class Product(db.Model):
    name = CharField()