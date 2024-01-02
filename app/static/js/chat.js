class Chat {
    constructor(messages, room_id, username) {
        this.messages = messages;
        this.room_id = room_id;
        this.username = username;
        this.last_msg_user = null
    }

    display() {
        document.getElementById('chat_rooms').hidden = true;
        document.getElementById('add_room').hidden = true;
        document.getElementById('add_room_form_btn').hidden = true;

        document.getElementById('chat').hidden = false;

        let chat_text = document.getElementById('chat_text')
        for (let i of this.messages){
            let li = document.createElement('li');
            li.innerHTML = i['content'];

            if (i['sender_name'] === this.username) {
                li.classList.add('own'); }
            else if (this.last_msg_user !== i['sender_name']){
                let name = document.createElement('li');
                name.innerHTML = i['sender_name'] + ":";
                chat_text.appendChild(name);
            }

            chat_text.appendChild(li);
            this.last_msg_user = i['sender_name'];
        }
    };

    displayNew() {
            let  chat_text = document.getElementById('chat_text');
            let li = document.createElement('li');

            let msg = this.messages[this.messages.length-1]

            li.innerHTML = msg['content'];


            if (msg['sender_name'] === this.username) { li.classList.add('own'); }
            else if (msg['sender_name'] !== this.last_msg_user){
                let name = document.createElement('li');
                name.innerHTML = msg['sender_name'] + ":";
                chat_text.appendChild(name);
            }

            chat_text.appendChild(li);
            this.last_msg_user = msg['sender_name'];
    }
    newMsg(msg) {
        this.messages.push(msg);
    }
}




