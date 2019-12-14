from models import product
from db import db
from exceptions import ProductNotFound

Product = product.Product
DataBase = db.DataBase()
ProductNotFoundException = ProductNotFound.ProductNotFoundException


class SellerController:
    pass