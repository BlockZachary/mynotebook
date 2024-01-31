# -*- coding:utf-8 -*-
# Author: Zachary
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ArticleForm(FlaskForm):
    title = StringField(label='标题', validators=[DataRequired()])
    content = TextAreaField(label='内容', validators=[DataRequired()])
    submit = SubmitField(label='提交')
