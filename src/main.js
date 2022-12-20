const socket = new WebSocket('ws://localhost:8001');

socket.addEventListener('open', (event) => {
    console.log('Connected to server');
});

socket.addEventListener('close', (event) => {
    console.log('Disconnected from server', event.data);
});

function dummy() {
    socket.send("");
}

function sendMessage() {
    var message = document.getElementById("id1").value;
    socket.send(message);
    console.log('Message sent to server');
    dummy();

}

socket.addEventListener('message', (event) => {
    console.log('Message from server ', event.data);
    document.getElementById("id2").value = event.data;
});