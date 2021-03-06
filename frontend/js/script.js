let button = document.getElementById("SolveButton")
let input = document.getElementById("InstanceInput")


function SetSolution(solution){
    let div = document.getElementsByClassName("solution")[0]
    div.innerHTML = "<span>Решение:</span><br>"
    for (let i = 0; i < solution.length; i++){
        div.innerHTML += `<li class="list-group-item">${i+1}. ${solution[i]}</li>`
    }
}


function SetTable (table){
    let keys = Object.keys(table)

    keys.sort(function (a, b){
        if (isNaN(parseInt(a))){
            if (isNaN(parseInt(b))){
                if (a > b){
                    return 1
                }else {return -1}
            }
            return -1
        }
        else{
            return 1
        }
    })

    let thead = document.getElementById("headers")
    thead.innerHTML = ''
    for (const [key] of keys) {

        thead.insertAdjacentHTML('beforeend', `<th scope="col">${key}</th>`)

    }
    let body = document.getElementById("body")
    body.innerHTML = ""
    let row = ""
    for (let i = 0; i < table[keys[0]].length; i++) {
        for (let j=0; j<keys.length; j++) {
            let value = table[keys[j]]
            row += `<td>${value[i]}</td>`
        }
        body.insertAdjacentHTML('beforeend', `<tr>${row}</tr>`)
        row = ""
    }
}


button.onclick = async function onclick () {
    let params = "?instance=" + input.value
    let request = await fetch("http://127.0.0.1:8000/solve_instance" + params, {
        method: "POST",
        headers: {
            "Accept": "application/json"
        }
    })
    let response = await request.json()
    if (response["status_code"] === 200){

        SetTable(response["truth_table"])
        SetSolution(response["solution"])
    }
    else{
        alert(response["detail"])
    }
}
