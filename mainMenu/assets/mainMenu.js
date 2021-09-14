let button = document.getElementById("OpenButton");
let message = document.getElementById("message");


function sleep(ms) {
  const wakeUpTime = Date.now() + ms;
  while (Date.now() < wakeUpTime) {}
}

const requestDoor = async () => {
    const wait = (timeToDelay) => new Promise((resolve) => setTimeout(resolve, timeToDelay))
    const response = await fetch('api/door', {
        method: 'POST',
        body:JSON.stringify({"open": true})
    });
    while (true) {
        const resp = await fetch('api/door', {
            method: 'GET',
        });
        let response = await resp.json();
        redirect(response);
        wait(1000)
    }
}

function redirect(response) {
    console.log(response)
    console.log(response["Result"])
    if (response["Result"] == "tutorial") {
        window.location.href = "/tutorial"
    } else if (response["Result"] == "feedback") {
        window.location.href = "/feedback?ID=" + String(response["ID"])
    } else if (response["Result"] == "kicked" || response["Result"] == "waiting") {
        message.textContent = "쓰레기를 넣은 후 문을 닫아 주세요"
    }
}
