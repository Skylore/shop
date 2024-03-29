from models import user


class DataBase:
    def __new__(cls):
        if not hasattr(cls, 'instance'):

            cls.instance = super(DataBase, cls).__new__(cls)
            cls.instance.users = dict()      # {login: user}
            cls.instance.products = dict()   # {product_id: product}
            cls.instance.product_requests = []
            cls.instance.support_requests = dict()
        else:
            # handle = open('../db/logs.txt', 'r')
            pass

        return cls.instance

    def login(self, login, password):
        if login not in self.users:
            raise FileNotFoundError
        elif self.users[login].getPassword() != password:
            raise PermissionError
        elif self.users[login].getPassword() == password:
            return self.users[login]

    def sign_up(self, name: str, login: str, password: str) -> user.User:
        if login in self.users:
            raise AssertionError

        u = user.User(name, login, password, 'customer')
        self.users[login] = u

        return u

    def __str__(self):
        return "\n".join(('{}: {}'.format(i, str(self.users[i])) for i in self.users))
