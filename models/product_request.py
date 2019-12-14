class ProductRequest:
    def __init__(self, login, product):
        self.__status = 'active'
        self.__login = login
        self.__product = product