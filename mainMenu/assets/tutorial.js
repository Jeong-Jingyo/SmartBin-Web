let done

const tutorial = async () => {
    let res_json
    while (true){
        let now = new Date()
        let response = await fetch("/api/end", {method: 'GET'})
        res_json = JSON.parse(await response.json());
        done = res_json["done"]
        Redirect(res_json)
    }
}

function Redirect(response) {
    console.log(response)
    if (response["done"] === false) {
        window.location.href = "/"
    }
}

async function Terminate() {
    while (done === true) {
        await fetch("/api/terminate", {
            method: "POST",
            body: JSON.stringify({"terminate": true}),
            headers: {'Content-Type': 'application/json'}
        })
    }

}

tutorial()
