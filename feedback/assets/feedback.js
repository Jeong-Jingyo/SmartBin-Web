let Category = null;
let ForeignSubst = null


function selectCategory(category) {
    Category = category
}

function selectForeignSubst(existence) {
    ForeignSubst = existence
}

const submitCategory = async() =>{
    if (Category !== null && ForeignSubst !== null){
        let body = {}
        body["feedback_type"] = Category
        body["feedback_foreign_subst"] = ForeignSubst
        console.log(body)
        let response = await fetch("api/feedback?ID=" + ID, {
            method: 'POST',
            body: JSON.stringify(body),
            headers: {'Content-Type': 'application/json'}
        })
        Redirect(JSON.parse(await response.json()))
    }
}

function Redirect(response) {
    console.log(response)
    if (response["Result"] === true) {
        window.location.href = "/tutorial"
    }
}

let ID = new URL(window.location.href).searchParams.get("ID")
