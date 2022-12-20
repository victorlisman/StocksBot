const socket = new WebSocket('ws://localhost:8001');

socket.addEventListener('open', (event) => {
    console.log('Connected to server');
});

socket.addEventListener('close', (event) => {
    console.log('Disconnected from server', event.data);
});

function sendMessage() {
    var message = document.getElementById("id1").value;
    socket.send(message);
    console.log('Message sent to server');
    return message;
}

socket.addEventListener('message', (event) => {
    console.log('Message from server ', event.data);
    document.getElementById("id2").value = event.data;
});