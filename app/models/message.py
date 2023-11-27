from app.db import init_db, Messages
from app.models.rooms import Room

db = init_db()


class Message:
    def __init__(self, sender, content, room, id=None, timestamp=None):
        self.sender = sender
        self.content = content
        self.room = room
        self.id = id
        self.timestamp = timestamp

    @staticmethod
    def get_by_room(room_id):
        with db.Session as s:
            messages = s.get(Messages, room_id).order_by(Messages.id)

        return Message(messages.sender, messages.content, Room.find_by_id(messages.room),
                       messages.id, messages.timestamp)

    @staticmethod
    def new_message(message):
        with db.begin() as s:
            new_message = Messages(content=message.content, sender=message.sender,
                                   room=message.room.room_id)
            s.add(new_message)

