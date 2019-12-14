class User:
    def __init__(self, name, login, password, role):
        self.__name = name
        self.__login = login
        self.__password = password
        self.__role = role
        self.__is_blocked = False

    def getName(self):
        return self.__name

    def getLogin(self):
        return self.__login

    def getPassword(self):
        return self.__password

    def getRole(self):
        return self.__role

    def getBlock(self):
        return self.__is_blocked


    def setName(self, name):
        self.__name = name

    def setLogin(self, login):
        self.__login = login

    def setPassword(self, password):
        self.__password = password

    def setRole(self, role):
        self.__role = role

    def setBlock(self, block):
        self.__is_blocked = block

    def __str__(self):
        return 'Name = {}, Login = {}, Password = {}, Role = {}, {}'.format(self.__name,self.__login,self.__password,self.__role,self.__is_blocked)

    def __eq__(self, other):
        return self.__name == other.getName()
