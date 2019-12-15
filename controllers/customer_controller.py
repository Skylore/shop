from models import product_request
from models import support_request
from db import db
from exceptions import ProductNotFound
import random

ProductRequest = product_request.ProductRequest
SupportRequest = support_request.SupportRequest
DataBase = db.DataBase()

ProductNotFoundException = ProductNotFound.ProductNotFoundException


class CustomerController:
    def __init__(self, user):
        self.__user = user

    @staticmethod
    def all_products():
        return (DataBase.products[i] for i in DataBase.products)

    def buy_product(self, product_id):

        if product_id in DataBase.products:
            prod = DataBase.products.pop(product_id)
            req = ProductRequest(self.__user.getLogin(), prod)

            DataBase.product_requests.append(req)
        else:
            raise ProductNotFoundException

    def ask(self, question):

        while True:
            id = random.randint(0, 10000)

            if id not in DataBase.support_requests:
                req = SupportRequest(self.__user.getLogin(), question)
                DataBase.support_requests[id] = req

                break

    def bought_products(self):
        return (i for i in DataBase.product_requests
                if i.getLogin() == self.__user.getLogin() and i.getStatus() == 'sold')

    def active_requests(self):
        return (i for i in DataBase.product_requests
                if i.getLogin() == self.__user.getLogin() and i.getStatus() == 'active')

    def questions(self):
        return (i for i in DataBase.support_requests
                if i.getLogin() == self.__user.getLogin and i.getStatus() == 'active')

    def support_answers(self):
        return (i for i in DataBase.support_requests
                if i.getLogin() == self.__user.getLogin and i.getStatus() == 'resolved')

