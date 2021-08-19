let button = document.getElementById("OpenButton");

function sleep(ms) {
  const wakeUpTime = Date.now() + ms;
  while (Date.now() < wakeUpTime) {}
}

const lockDoor = async() => {
    let body = {}
    body["open"] = true

    console.log(JSON.stringify(body))
    const response = await fetch('api/door', {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {'Content-Type': 'application/json'}
    });
    window.location.href = '/tutorial'
}
