# -*- coding:utf-8 -*-
# Author: Zachary
from flask import render_template, abort, flash, redirect, url_for, send_from_directory
from flask_login import current_user, logout_user

from common.profile import Profile
from forms.article_delete_form import ArticleDeleteForm
from forms.login_form import LoginForm
from routes import app
from services.article_service import ArticleService
from services.user_service import UserService


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def home_page():
    articles = ArticleService().get_articles()
    if current_user.is_authenticated:
        article_delete_form = ArticleDeleteForm()
        if article_delete_form.validate_on_submit():
            try:
                ArticleService().delete_article(int(article_delete_form.article_id.data))
                flash(f'文章删除成功', category='success')
                return redirect(url_for('home_page'))
            except Exception as e:
                flash(f'文章删除失败: {e}', category='danger')
        return render_template('index.html', articles=articles, article_delete_form=article_delete_form)
    return render_template('index.html', articles=articles)


@app.route('/article/<article_id>')
def article_page(article_id):
    article = ArticleService().get_article_by_id(article_id)
    if article:
        return render_template('article.html', article=article)
    abort(404)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        result = UserService().do_login(form.account.data, form.password.data)
        if result:
            flash(f'{form.account.data}登录成功, 正在跳转...', category='success')
            return redirect(url_for('home_page'))
        else:
            flash(f'{form.account.data}登录失败， 请检查账号密码', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    return redirect(url_for('home_page'))


@app.route('/image/<image_filename>')
def download_image(image_filename: str):
    image_path = Profile.get_image_path()
    image_filepath = image_path.joinpath(image_filename)
    if not image_filepath.exists():
        abort(404)
    return send_from_directory(directory=image_path, path=image_filename)
