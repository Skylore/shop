class SupportRequest:
    def __init__(self, login, user_message):
        self.__login = login
        self.__user_message = user_message
        self.__support_message = ""
        self.__status = 'active'


    def getLogin(self):
        return self.__login


    def getUserMessage(self):
        return self.__user_message


    def getSupportMessage(self):
        return self.__support_message


    def getStatus(self):
        return self.__status


    def setLogin(self, login):
         self.__login = login


    def setUserMessage(self, user_message):
        self.__user_message = user_message


    def setSupportMessage(self, support_message,):
        self.__support_message = support_message
        self.__status = 'resolved'









