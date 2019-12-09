class DataBase:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DataBase, cls).__new__(cls)
            cls.instance.users = []
            cls.instance.products = []
            cls.instance.product_requests = []
            cls.instance.sold_products = []
            cls.instance.support_requests = []
        return cls.instance
