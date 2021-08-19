Category = null
ForeignSubst = null


function selectCategory(category) {
    Category = category
    if (ForeignSubst !== null) {
        const promise = submitCategory();
    }
}

function selectForeignSubst(existence) {
    ForeignSubst = existence
    if (Category !== null) {
        const promise = submitCategory();
    }
}

const submitCategory = async() =>{
    let body = {}
    body["Category"] = Category
    body["ForeignSubst"] = ForeignSubst
    let response = await fetch("api/feedback", {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {'Content-Type': 'application/json'}
    })
}