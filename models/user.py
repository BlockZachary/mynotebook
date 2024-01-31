# -*- coding:utf-8 -*-
# Author: Zachary
import crypt

import bcrypt
from flask_login import UserMixin
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from routes import db, login_manager


@login_manager.user_loader
def load_manager_user(user_id: int):
    return db.session.get(User, user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    account: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)

    def password_check(self, password):
        return bcrypt.checkpw(password.encode(), self.password.encode())
