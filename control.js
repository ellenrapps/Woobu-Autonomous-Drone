// Developed by Ellen Red


var buttonSelector = document.querySelectorAll('button');
buttonSelector.forEach(function (el){
    el.addEventListener("click", function(ev){
        buttonSelector.forEach(function(button) { button.style.opacity = '0.5' })
        this.style.opacity = 1
    })
});

document.addEventListener("DOMContentLoaded", function(event) {
    const getSensorReadings = function() {
        fetch('/update')
            .then((resp) => resp.json())
            .then(function(response) {
                document.getElementById('x_angle').innerHTML =response.kalman_x_angle;
                document.getElementById('y_angle').innerHTML =response.kalman_y_angle;
        });
    }

    getSensorReadings();
    setInterval(getSensorReadings, 10);  // update every 10 milliseconds
});


var targetUrl = `ws://${location.host}/ws`;
var websocket;
window.addEventListener("load", onLoad);

function onLoad() {
  initializeSocket();
}

function initializeSocket() {
  websocket = new WebSocket(targetUrl);
  websocket.onopen = onOpen;
  websocket.onclose = onClose;
  websocket.onmessage = onMessage;
}

function onOpen(event) {
  console.log("Websocket Open...");
}

function onClose(event) {
  console.log("Websocket Close...");
  setTimeout(initializeSocket, 2000);
}

function onMessage(event) {
  console.log("WebSocket message received:", event);
}

function sendMessage(message) {
  websocket.send(message);
}

function auto_takeoff() {
    sendMessage(auto_takeoff);
}

function hover() {
    sendMessage(hover);
}


function down() {
    sendMessage(down);
}


function on_manual() {
    sendMessage(on_manual);
}


function off_manual() {
     sendMessage(off_manual);
}




