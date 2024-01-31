# -*- coding:utf-8 -*-
# Author: Zachary
from sqlalchemy import Select, func, and_

from models.article import Article
from routes import db


class ArticleService:
    def get_article_by_id(self, article_id):
        return db.session.get(Article, article_id)

    def get_articles(self):
        query = Select(Article)
        return db.session.scalars(query).all()

    def add_article(self, article: Article):
        # 先查询是否已经存在
        query = Select(Article).where(Article.title == article.title)
        if db.session.scalar(query):
            # 抛出异常
            raise Exception('该标题文章已经存在，请重新编辑')
        db.session.add(article)
        db.session.commit()
        return article

    def update_article(self, article: Article):
        # 先查询是否已经存在
        existed_article = self.get_article_by_id(article.id)
        if not existed_article:
            raise Exception('该文章不存在')
        # 查询要更新的文章标题是否已经存在
        query = Select(Article).where(and_(Article.title == article.title, Article.id != article.id))
        if db.session.scalar(query):
            raise Exception('该标题文章已经存在，请重新编辑')
        # 更新
        existed_article.title = article.title
        existed_article.content = article.content
        existed_article.update_time = func.now()

        db.session.commit()
        return article

    def delete_article(self, article_id: int):
        article = self.get_article_by_id(article_id)
        if not article:
            raise Exception('该文章不存在')
        db.session.delete(article)
        db.session.commit()
        return article
