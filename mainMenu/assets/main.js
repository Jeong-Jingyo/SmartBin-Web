let button = document.getElementById("OpenButton");

const Door = async() => {
    let body = {}
    body["open"] = true
    console.log(JSON.stringify(body))
    const response = await fetch('api', {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {'Content-Type': 'application/json'}
    });
}