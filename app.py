from sqlalchemy import inspect

from routes import app, db
import bcrypt


def init_db():
    with app.app_context():
        inspector = inspect(db.engine)
        if not inspector.has_table('users'):
            from models.user import User
            from models.article import Article
            db.create_all()
            hashed_password = bcrypt.hashpw("123456".encode(), bcrypt.gensalt())
            user = User(account="zachary", password=hashed_password.decode(), username="zachary")
            db.session.add(user)
            db.session.commit()


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', debug=True, port=8080)
