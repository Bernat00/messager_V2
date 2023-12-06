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
        messages = []
        with db.Session() as s:
            query = s.scalars(Messages.select().order_by(Messages.timestamp))

            for message in query:
                messages.append(
                    Message(message.sender, message.content, message.room, message.id, message.timestamp)
                )

        return messages

    @staticmethod
    def new_message(message):
        with db.begin() as s:
            new_message = Messages(content=message['content'], sender=message['sender'],
                                   room=message['room_id'])
            s.add(new_message)

    def to_dict(self):
        tmp = {
            'sender': self.sender,
            'content': self.content,
            'room': self.room,
            'id': self.id,
            'timestamp': self.timestamp
        }

        return tmp

