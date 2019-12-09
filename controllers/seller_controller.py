from models import product
from db import db

Product = product.Product
DataBase = db.DataBase()


class SellerController:
    def __init__(self, user):
        self.__user = user

    def getUser(self):
        return self.__user

    """Implement NON static methods here"""
