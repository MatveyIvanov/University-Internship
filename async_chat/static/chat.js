const socket = new WebSocket('ws://localhost:8000');
var connected = false;

socket.onopen = function (event) {
    console.log("Websocket opened ...")
};
socket.onmessage = function (event) {
    data = JSON.parse(event.data);
    if (data['event'] == 'error') {
        alert(data['errors']);
    }
    else if (data['event'] == 'auth') {
        console.log(data['data']['message']);
        document.querySelector('#username_input').readOnly = true;
        document.querySelector('#message_input').readOnly = false;
        document.querySelector('#send_button').textContent = 'Send';
        connected = true;
    }
    else if (data['event'] == 'message') {
        chat_log = document.querySelector('#chat_log');
        chat_log.value += "\n" + data['data']['username'] + ": " + data['data']['message'];
    }
};
socket.onclose = function (event) {
    console.log("Websocket closed ...");
};

const sendMessage = () => {
    if (connected == false) {
        authToChat();
        return;
    }
    username = document.querySelector('#username_input').value;
    message = document.querySelector('#message_input').value;
    if (message != '' && message != null) {
        socket.send(JSON.stringify({
            'event': 'message',
            'data': {
                'username': username,
                'message': message
            }
        }));
    }
}

const authToChat = () => {
    username = document.querySelector('#username_input').value;
    if (username == '' || username == null) {
        alert("Для подключения к чату введите ник");
        return;
    }
    socket.send(JSON.stringify({
        'event': 'auth',
        'data': {
            'username': username
        }
    }));
}

document.querySelector('#send_button').onclick = sendMessage;