import random

from models import product
from db import db
from exceptions import ProductNotFound, ResolvedProductRequestException

Product = product.Product
DataBase = db.DataBase()
ProductNotFoundException = ProductNotFound.ProductNotFoundException
ResolvedProductRequestException = ResolvedProductRequestException.ResolvedProductRequestException


class SellerController:
    def __init__(self, user):

        if user.getRole() != 'seller':
            raise PermissionError

        self.__user = user

    def add_product(self, product_name, product_desc):
        while True:
            prod_id = random.randint(0, 1000)

            if prod_id not in DataBase.products:
                prod = Product(prod_id, product_name, product_desc, self.__user.getLogin())
                DataBase.products[prod.getProductId()] = prod

                return prod

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
                and i.getProduct().getOwner() == self.__user.getLogin())

    def accept_request(self, product_id):

        for i in DataBase.product_requests:
            prod = i.getProduct()
            if prod.getProductId() == product_id:
                if prod.getOwner() == self.__user.getLogin():
                    i.sell()
                    return
                else:
                    raise PermissionError

        raise ProductNotFoundException

    def reject_request(self, product_id):

        for i in DataBase.product_requests:
            prod = i.getProduct()
            if prod.getProductId() == product_id:
                if prod.getOwner() == self.__user.getLogin():
                    if i.getStatus() == 'active':
                        self.add_product(prod.getProductName(), prod.getProductDesc())
                        DataBase.product_requests.remove(i)

                        return
                    else:
                        raise ResolvedProductRequestException
                else:
                    raise PermissionError

        raise ProductNotFoundException





