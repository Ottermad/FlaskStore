from app.models import Role, UserRoles, User, Product
from app import db

for model in [Role, UserRoles, User, Product]:
    model.create_table()