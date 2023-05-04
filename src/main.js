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

document.getElementById("id1").addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});

function addToPortofolio() {
    document.getElementById("myModal").style.display = "block";
    var modal = document.getElementById("myModal");
    var button = document.getElementById("close");
    var addStock = document.getElementById("addS");

    button.onclick = function() {
        modal.style.display = "none";
    }

    addStock.onclick = function() {
        var stockName = document.getElementById("sname").value;
        var stockPrice = document.getElementById("sprice").value;
        var stockQuantity = document.getElementById("squantity").value;
        var stock = {
            "stockName": stockName,
            "stockPrice": stockPrice,
            "stockQuantity": stockQuantity
        }

        var newStock = document.createElement("div");
        newStock.style.whiteSpace = "pre-wrap";
        newStock.style.margin = "10px";
        newStock.innerHTML = "Stock Name: " + stockName + " | " + "Stock Price: " + stockPrice + " | " + "Stock Quantity: " + stockQuantity;
        document.getElementById("portItems").appendChild(newStock);

        document.getElementById("sname").value = "";
        document.getElementById("sprice").value = "";
        document.getElementById("squantity").value = "";
        
        modal.style.display = "none";


    }
}