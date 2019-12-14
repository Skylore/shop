import random
from models import product
from db import db
from exceptions import ProductNotFound

Product = product.Product
DataBase = db.DataBase()
ProductNotFoundException = ProductNotFound.ProductNotFoundException


class SellerController:
    def __init__(self,user):
        self.__user = user
    def add_product(self, product_name, product_desc):
        while True:
            prod_id = random.randint(0,1000)
            if prod_id not in DataBase.products:
                prod = Product(prod_id,product_name,product_desc, self.__user.getLogin())
                DataBase.products[prod.getProductId()] = prod

                break

    def remove_product(self, product_id):
        if product_id not in DataBase.products:
            raise ProductNotFoundException
        elif self.__user.getLogin() != DataBase.products[product_id].getOwner():
            raise PermissionError
        return DataBase.products.pop(product_id)
    def my_products(self):
        array = []
        for i in DataBase.products:
            if self.__user.getLogin() == DataBase.products[i].getOwner():
                array.append(DataBase.products[i])
        print('Your products: ', ', '.join(array))
        return array
    def accept_request(self,product_id):
        if product_id not in DataBase.products:
            raise ProductNotFoundException
        elif self.__user.getLogin() != DataBase.product_requests.getProduct().getOwner():
            raise PermissionError
    def product_requests(self):
        return (i for i in DataBase.product_requests
               if i.getStatus() == 'active'
               and i.getProduct().getOwner() == self.__user.getLogin())








