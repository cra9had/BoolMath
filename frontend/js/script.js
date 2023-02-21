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


window.addEventListener('load', function () {
    let keyboard = document.getElementById('keyboard')
    let buttons = ['/\\', '\\/', '->', '=', 'INV()', 'A', 'B', 'C', 'D'];
    console.log(buttons)
    for (let i = 0; i < buttons.length; i++){
        const button_text = buttons[i]
        const button = `<button class="keyboard-button" id="${button_text}">${button_text}</button>`
        keyboard.insertAdjacentHTML('beforeend', button)
        document.getElementById(button_text).onclick = function () {
            const length = input.selectionStart

            input.setRangeText(button_text)
            input.focus()
            if (button_text !== "INV()") {
                input.setSelectionRange( length + button_text.length,  length + button_text.length);
            } else {
                input.setSelectionRange( length + button_text.length - 1,  length + button_text.length - 1);
            }
        }
    }
})

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


function pop(event) {
  const amount = 50; // particle amount
  let x = event.clientX,
    y = event.clientY + window.scrollY;
  const create = (x, y) => {
    for (let i = 0; i < amount; i++)
      createParticle(x, y, event.target.dataset.particle);
  };
  // check if the button gots clicked with the keyborad
  if (event.clientX === 0 && event.clientY === 0) {
    const box = event.target.getBoundingClientRect();
    x = box.left + box.width / 2;
    y = box.top + box.height / 2;
  }
  create(x, y);
}
function createParticle(x, y, img) {
  const image = 'static/images/atom.png'
  const particle = document.createElement("particle");
  document.body.appendChild(particle);
  // just play a little bit with these values 🙂
  const size = Math.floor(Math.random() * 28 + 4);
  const destinationX = (Math.random() - 0.5) * 150;
  const destinationY = (Math.random() - 0.5) * 150;
  const rotation = Math.random() * 500;
  const duration = Math.random() * 1000 + 1000;
  const delay = Math.random() * 200;
  particle.style.backgroundImage = `url(${image})`;
  particle.style.width = particle.style.height = `${size}px`;
  const animation = particle.animate(
    [
      {
        transform: `translate(-50%, -50%) translate(${x}px, ${y}px) rotate(0deg)`,
        opacity: 1
      },
      {
        transform: `translate(-50%, -50%) translate(${x + destinationX}px, ${
          y + destinationY
        }px) rotate(${rotation}deg)`,
        opacity: 0
      }
    ],
    {
      duration,
      easing: "cubic-bezier(0, .9, .57, 1)",
      delay
    }
  );
  animation.onfinish = removeParticle;
}
function removeParticle(event) {
  event.srcElement.effect.target.remove();
}
if (document.body.animate) document.body.addEventListener("click", pop);
