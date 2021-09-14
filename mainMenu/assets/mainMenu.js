let button = document.getElementById("OpenButton");
let message = document.getElementById("message");


function sleep(ms) {
  const wakeUpTime = Date.now() + ms;
  while (Date.now() < wakeUpTime) {}
}

const requestDoor = async () => {
    const response = await fetch('api/door', {
    });
    setTimeout(async () => {
        const resp = await fetch('api/door', {
            method: 'GET',
        });
        let response = await response.json();
        redirect(response);
    }, 1000);
}

function redirect(response) {
    console.log(response)
    console.log(response["Result"])
    if (response["Result"] == "tutorial") {
        window.location.href = "/tutorial"
    } else if (response["Result"] == "feedback") {
        window.location.href = "/feedback?ID=" + String(response["ID"])
    } else if (response["Result"] == "kicked" && response["Result"] == "waiting") {
        message.textContent = "쓰레기를 넣고 문을 닫아 주세요"
    }
}
