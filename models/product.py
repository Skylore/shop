class Product:
    def __init__(self, product_id, product_name, product_desc, owner):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__product_desc = product_desc
        self.__owner = owner


    def getProductId(self):
        return self.__product_id


    def getProductName(self):
        return self.__product_name


    def getProductDesk(self):
        return self.__product_desc


    def getOwner(self):
        return self.__owner


    def setProductId(self, product_id):
        self.__product_id = product_id


    def setProductName(self, product_name):
        self.__product_name = product_name


    def setProductDesk(self, product_desc):
        self.__product_desc = product_desc


    def setOwner(self, owner):
        self.__owner = owner


    def __str__(self):
        return 'product id: {}, product name: {}, product description: {}, owner: {}'.format(self.__product_id, self.__product_name, self.__product_desc, self.__owner)


    def __eq__(self, other):
        if self.product_id == other.getProductId():
            return



