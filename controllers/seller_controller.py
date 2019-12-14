import random

from models import product
from db import db
from exceptions import ProductNotFound

Product = product.Product
DataBase = db.DataBase()
ProductNotFoundException = ProductNotFound.ProductNotFoundException


class SellerController:
    def __init__(self, user):
        self.__user = user

    def add_product(self, product_name, product_desc):
        while True:
            prod_id = random.randint(0, 1000)

            if prod_id not in DataBase.products:
                prod = Product(prod_id, product_name, product_desc, self.__user.getLogin())
                DataBase.products[prod.getProductId()] = prod

                break

    def remove_product(self, product_id):

        if product_id not in DataBase.products:
            raise ProductNotFoundException
        elif self.__user.getLogin() != DataBase.products[product_id].getOwner():
            raise PermissionError

        return DataBase.products.pop(product_id)

    def my_products(self):

        return (DataBase.products[i] for i in DataBase.products
                if DataBase.products[i].getOwner() == self.__user.getLogin())

    def product_requests(self):
        # res = []

        # for i in DataBase.product_requests:
        #     if i.getStatus() == 'active' and i.getProduct().getOwner() == self.__user.getLogin():
        #         res.append(i)

        return (i for i in DataBase.product_requests
                if i.getStatus() == 'active'
                and i.getProduct().getOwner() == self.__user.getLogin)
