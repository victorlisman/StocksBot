const socket = new WebSocket('ws://localhost:8001');

socket.addEventListener('open', (event) => {
    console.log('Connected to server');
});

socket.addEventListener('close', (event) => {
    console.log('Disconnected from server', event.data);
});

//fucntion to send data to server from client
function sendMessage() {
    var message = document.getElementById("id1").value;
    console.log('Message from client ', message);
    socket.send(JSON.stringify(message));
    document.getElementById("chat-window").innerHTML += "You: " + message + '\n';
}

socket.addEventListener("message", ({ data }) => {
    console.log("Message from server ", JSON.parse(data));
    document.getElementById("chat-window").innerHTML += "Bot: " + JSON.parse(data) + '\n';
});