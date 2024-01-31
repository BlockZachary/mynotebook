# -*- coding:utf-8 -*-
# Author: Zachary
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField


class ImageUploadForm(FlaskForm):
    image = FileField(label='上传图片', validators=[FileRequired()])
    submit = SubmitField(label='上传')
