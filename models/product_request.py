class ProductRequest:
    def __init__(self, login, product):
        self.__status = 'active'
        self.__login = login
        self.__product = product

    def getStatus(self):
        return self.__status

    def getLogin(self):
        return self.__login

    def getProduct(self):
        return self.__product

    def setStatus(self, status):
        self.__status = status

    def setLogin(self, login):
        self.__login = login

    def setProduct(self, product):
        self.__product = product

    def switchStatus(self):
        if self.__status == 'active':
            self.__status = 'sold'
        else:
            self.__status = 'active'

    def __str__(self):
        return 'Login = {}, Product = {}, Status = {}'.format(self.__login, self.__product, self.__status)
