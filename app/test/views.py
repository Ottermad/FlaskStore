from app.test.models import Test
from flask import Blueprint

test = Blueprint("test", __name__)

@test.route("/")
def home():
    names = Test.get_names()
    return str(names)