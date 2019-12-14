class User:
    def __init__(self, name, login, password, role):
        self.__name = name
        self.__login = login
        self.__password = password
        self.__role = role
        self.__is_blocked = False
