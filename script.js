function sendCommand(command) {
    fetch('http://localhost:5000/command', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ command: command })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.response;
    })
    .catch(error => console.error('Error:', error));
}
