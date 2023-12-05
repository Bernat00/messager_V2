import app.db
from app.db import RoomUser, Rooms
from app.models.user import User

db = app.db.init_db()


class Room:
    def __init__(self, room_name, members, room_id=None):
        self.room_name = room_name
        self.members = members
        self.room_id = room_id

    @staticmethod
    def save(room):
        if room.room_id is not None:
            with db.begin() as session:
                new_room = Rooms(room_name=room.room_name)
                session.add(new_room)

                for member in room.members:
                    session.add(RoomUser(user_id=member, room_id=room.room_id))

    @staticmethod
    def find_by_id(room_id):
        with db.Session() as s:
            room = s.get(Rooms, room_id)
            menbers = s.scalars(RoomUser.select().where(room_id=room_id)).user_id

        return Room(room.room_name, menbers, room_id)

    @staticmethod
    def get_rooms_by_user_id(user_id):
        with db.Session() as s:
            room_ids = s.scalars(RoomUser.select().where(RoomUser.user_id == user_id))
        rooms = []
        for id in room_ids:
            rooms.append(Room.find_by_id(id).room_id)

        return rooms

    @staticmethod
    def get_rooms_name_and_user(name, username):
        user_id = User.find_by_username(username)
        rooms = Room.get_rooms_by_user_id(user_id)

        for room in rooms:
            if name not in room.members:
                rooms.remove(room)

        return rooms

    def to_dict(self):
        tmp = {
            'room_id': self.room_id,
            'room_name': self.room_name,
            'members': self.members
        }

