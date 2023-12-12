from werkzeug.security import generate_password_hash, check_password_hash

from app.db import Users, init_db

db = init_db()


class User:
    def __init__(self, username, email, digest=None, user_id=None,  password=None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.digest = digest
        self.password = password

    @property
    def password(self):
        return None

    @password.setter
    def password(self, value):
        if value and len(value) > 0:
            self.digest = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self.digest, password)

    @staticmethod
    def find_by_id(user_id):
        with db.Session() as session:
            user = session.scalar(Users.select().where(Users.id == user_id))
            if user is not None:
                return User(user.username, user.email, user.password, user.id)

        return None

    @staticmethod
    def find_by_username(username):
        with db.Session() as session:
            query = session.scalar(Users.select().where(Users.username == username))
            if query is None:
                return None
        return User(query.username, query.email, query.password, query.id)

    @staticmethod
    def save(user):
        if user.user_id:
            with db.begin() as s:
                user_db = s.get(Users, user.user_id)
                user_db.username = user.username
                user_db.email = user.email
                user_db.password = user.digest

        else:
            with db.begin() as s:
                user_db = Users(username=user.username, password=user.digest, email=user.email)
                s.add(user_db)

    @staticmethod
    def delete(user_id):
        with db.begin() as s:
            user = s.get(Users, user_id)
            s.delete(user)

    @staticmethod
    def get_all_tuple_incomplete():
        with db.Session() as s:
            users = s.scalars(Users.select())

            user_tuples = []
            for user in users:
                user_tuples.append((user. id, user.username))

        return user_tuples


