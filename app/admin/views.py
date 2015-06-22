from app.models import Product
from flask import Blueprint

admin = Blueprint("admin", __name__, url_prefix="/admin")

@admin.route("/")
def home():
    #names = Test.get_names()
    #return str(names)
    return "Hi"