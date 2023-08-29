function sendCoordinates(latitude, longitude) {
    const url = '/getlink';
    const data = {
        latitude: latitude,
        longitude: longitude
    };

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Response from server:', data);
		window.location.href = data.link;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            sendCoordinates(latitude, longitude);
        }, error => {
            console.error('Error getting location:', error);
        });
    } else {
        console.error('Geolocation is not supported by this browser.');
    }
}

getLocation();
