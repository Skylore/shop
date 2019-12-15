from db import db
from exceptions import SupportRequestNotFound

DataBase = db.DataBase()
SupportRequestNotFoundException = SupportRequestNotFound.SupportRequestNotFoundException


class SupportController:

    def __init__(self, user):
        if user.getRole() != 'support':
            raise PermissionError

    def support_requests(self):
        return (DataBase.support_requests[i] for i in DataBase.support_requests
                if i.getStatus() == "active")

    def answer(self, message, req_id):

        if req_id not in DataBase.support_requests:
            raise SupportRequestNotFoundException

        DataBase.support_requests[req_id].setSupportMessage(message)
