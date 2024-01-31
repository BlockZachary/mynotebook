# -*- coding:utf-8 -*-
# Author: Zachary
from datetime import datetime

from sqlalchemy import Integer, String, BLOB, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column

from routes import db


class Article(db.Model):
    __tablename__ = 'articles'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    __content: Mapped[bytes] = mapped_column(BLOB, name='content', nullable=False)
    create_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, default=func.now())
    update_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True, default=func.now())

    @property
    def content(self):
        return self.__content.decode('utf-8')

    @content.setter
    def content(self, content: str):
        self.__content = content.encode()
