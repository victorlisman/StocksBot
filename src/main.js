const socket = new WebSocket('ws://localhost:8001');


socket.addEventListener('open', (event) => {
    console.log('Connected to server');
});

socket.addEventListener('close', (event) => {
    console.log('Disconnected from server', event.data);
});


function sendMessage() {
    var message = document.getElementById("id1").value;
    var chatBox = document.getElementById("chat-window");
    var newMessage = document.createElement("div");
    newMessage.style.whiteSpace = "pre-wrap";
    newMessage.innerHTML = "You: " + message;
    chatBox.appendChild(newMessage);
    socket.send(JSON.stringify(message));
    console.log('Message from client ', message);
    document.getElementById("id1").value = "";    
}

socket.addEventListener("message", ({ data }) => {
    console.log("Message from server ", JSON.parse(data));
    document.getElementById("chat-window").innerHTML += "\nBot: " + JSON.parse(data) + '\n';
});
