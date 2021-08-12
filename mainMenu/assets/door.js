let button = document.getElementById("OpenButton");

function sleep(ms) {
  const wakeUpTime = Date.now() + ms;
  while (Date.now() < wakeUpTime) {}
}

const openDoor = async() => {
    let body = {}
    body["open"] = true

    console.log(JSON.stringify(body))
    const response = await fetch('api/open', {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {'Content-Type': 'application/json'}
    });
}

const tutorial = async() => {
    while (true) {
        let response = await fetch('api/closed', {method: 'GET'})
            .then(function(response){ return response.json()})
        response = JSON.parse(response)
        if (response["closed"] === true) {
            window.location.href = "/tutorial"
        }
        sleep(1000)
    }
}

tutorial()