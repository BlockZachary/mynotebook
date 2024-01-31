# -*- coding:utf-8 -*-
# Author: Zachary
from flask_login import login_user, logout_user
from sqlalchemy import Select

from models.user import User
from routes import db


class UserService:

    def do_login(self, account: str, password: str) -> bool:
        query = Select(User).where(User.account == account)
        user = db.session.scalar(query)
        if user and user.password_check(password):
            login_user(user)
            return True
        return False
