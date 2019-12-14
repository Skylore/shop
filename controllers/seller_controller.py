import randome
from models import product
from db import db
from exceptions import ProductNotFound

Product = product.Product
DataBase = db.DataBase()
ProductNotFoundException = ProductNotFound.ProductNotFoundException


class SellerController:
    def __init__(self, user):
        self.user = user

    def add_product(self, product_name, product_desc):
        while True:
            prod_id = randome.randint(0, 1000)

            if prod_id not in DataBase.products:
                prod = Product(prod_id, product_name, product_desc, self.__user.getlogin())
                DataBase.products[prod.getProductId()] = prod

            break

    def remove_product(self, product_id):
        if product_id not in DataBase.products:
            raise ProductNotFoundException
        elif self.__user.detLogin() != DataBase.products[product_id].getOwner():
            raise PermissionError

        return DataBase.products.pop(product_id)

    def my_product(self):
        res = []
         for i in DataBase.products:
             if self.__user.getLogin() == DataBase.products[i].getOwner()
                 res.append(DataBase.products[i])

    def product_recuest(self):
        mas = []
        for i in DataBase.product_requests:
           if i.getStatus() == 'active' and i.getProduct().getOwner() == self.__user.getLogin():
               mas.append(i)

        return mas

