class SupportRequest:
    def __init__(self, login, user_message):
        self.__login = login
        self.__user_message = user_message
        self.__support_message = ""
        self.__status = 'active'
