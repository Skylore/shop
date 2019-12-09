from models import product_request
from models import support_request
from db import db

ProductRequest = product_request.ProductRequest
SupportRequest = support_request.SupportRequest
DataBase = db.DataBase()


class UserController:
    def __init__(self, user):
        self.__user = user

    def getUser(self):
        return self.__user

    """Implement NON static methods here"""
