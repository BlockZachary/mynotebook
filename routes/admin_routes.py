# -*- coding:utf-8 -*-
# Author: Zachary
from flask import flash, redirect, url_for, render_template, request
from flask_login import login_required
from werkzeug.utils import secure_filename

from common import utils
from common.profile import Profile
from forms.article_form import ArticleForm
from forms.image_upload_form import ImageUploadForm
from models.article import Article
from routes import app
from services.article_service import ArticleService
from services.image_service import ImageService


@app.route('/create_article', methods=['GET', 'POST'])
@login_required
def create_article_page():
    form = ArticleForm()
    if form.validate_on_submit():
        article = Article()
        article.title = form.title.data
        article.content = form.content.data

        try:
            ArticleService().add_article(article)
            flash(f'文章《{article.title}》创建成功', category='success')
            return redirect(url_for('home_page'))
        except Exception as e:
            flash(f'文章《{article.title}》创建失败: {e}', category='danger')
    return render_template('create_article.html', form=form, isEdit=False)


@app.route('/edit_article/<article_id>', methods=['GET', 'POST'])
@login_required
def edit_article_page(article_id: str):
    form = ArticleForm()
    # 点击编辑后 回显数据
    if request.method == 'GET':
        try:
            article = ArticleService().get_article_by_id(article_id)
            if not article:
                flash("文章不存在", category='danger')
                return redirect(url_for('home_page'))
            else:
                form.title.data = article.title
                form.content.data = article.content
        except Exception as e:
            flash(f'文章获取失败: {e}', category='danger')
            return redirect(url_for('home_page'))

    # 更新数据后 保存
    if form.validate_on_submit():
        article = Article()
        try:
            article.id = int(article_id)
            article.title = form.title.data
            article.content = form.content.data

            ArticleService().update_article(article)
            flash(f'文章《{article.title}》更新成功', category='success')
            return redirect(url_for('home_page'))
        except Exception as e:
            flash(f'文章《{article.title}》更新失败: {e}', category='danger')
    return render_template('create_article.html', form=form, isEdit=True)


@app.route('/images', methods=['GET', 'POST'])
@login_required
def images_page():
    form = ImageUploadForm()
    if form.validate_on_submit():
        image_file = form.image.data
        image_path = Profile.get_image_path()
        image_filename = secure_filename(image_file.filename)
        image_full_path = utils.get_save_filepath(image_path, image_filename)
        image_file.save(image_full_path)
        flash(f'图片上传成功, 保存至 {image_full_path}', category='success')

    image_filenames = ImageService().get_image_filename_list()
    return render_template('images.html', form=form, image_filenames=image_filenames)
