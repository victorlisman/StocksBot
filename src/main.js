const socket = new WebSocket('ws://localhost:8001');

socket.addEventListener('open', (event) => {
    console.log('Connected to server');
});

socket.addEventListener('close', (event) => {
    console.log('Disconnected from server', event.data);
});

const sendMessage = () => {
    socket.send(document.getElementById("id1").value);
    document.getElementById("id1").value = "";
}