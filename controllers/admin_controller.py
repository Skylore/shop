from db import db
from exceptions import UserNotFound

DataBase = db.DataBase()
UserNotFoundException = UserNotFound.UserNotFoundException


class AdminController:
    def __init__(self, user):
        if user.getRole() != 'admin':
            raise PermissionError

        self.user = user

    def set_role(self, login, role):
        if login not in DataBase.users:
            raise UserNotFoundException

        DataBase.users[login].setRole(role)

    def block_user(self, login):
        if login not in DataBase.users:
            raise UserNotFoundException

        DataBase.users[login].block()

    def unblock_user(self, login):
        if login not in DataBase.users:
            raise UserNotFoundException

        DataBase.users[login].unblock()

    def all_users(self):
        return (DataBase.users[i] for i in DataBase.users)

