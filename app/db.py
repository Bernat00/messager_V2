from sqlalchemy import String, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from alchemical import Alchemical, Model

from datetime import datetime


class Users(Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(128), unique=True)
    email: Mapped[str] = mapped_column(String(256))
    password: Mapped[str] = mapped_column(String(128))


class Messages(Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String(2000))
    sender: Mapped[int] = mapped_column()
    room: Mapped[str] = mapped_column()
    timestamp: Mapped[datetime] = mapped_column(server_default=func.now())


class Rooms(Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    room_name: Mapped[int] = mapped_column()


class RoomUser(Model):
    __tablename__ = 'room_message'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column()
    room_id: Mapped[int] = mapped_column()


def init_db():
    db = Alchemical("sqlite:///database.db")  # url_for('static', filename='favicon.png') ezzel működhet?
    db.create_all()
    return db
