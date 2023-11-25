from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column
from alchemical import Alchemical, Model


class Users(Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(128), unique=True)
    email: Mapped[str] = mapped_column(String(256))
    password: Mapped[str] = mapped_column(String(128))


class Messages(Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    sender: Mapped[int] = mapped_column()
    recipient: Mapped[int] = mapped_column()
    timestamp: Mapped[int] = mapped_column(server_default=func.now())


def init_db():
    db = Alchemical("sqlite:///database.db")  # url_for('static', filename='favicon.png') ezzel működhet?
    db.create_all()
    return db
