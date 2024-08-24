let list = document.getElementById("msgs");
let id = document.querySelector("#id").value;
let sender = document.querySelector("#sender");
let input = document.querySelector("input[name=msg]");
let number_of_msgs = 0;
function live() {
    $.ajax({
        url: `get/${id}`,
        data: {
            get: "n"
        },
        success: function (result) {
            if (number_of_msgs != result["number"]) {
                $.ajax({
                    url: `get/${id}`,
                    data: {
                        get: "msgs"
                    },
                    success: function (results) {
                        list.innerHTML = "";
                        addData(results);
                        number_of_msgs = result["number"];
                    }
                });
            }
        }
    });
}
function addData(data) {
    let d = Array();
    d = data["msgs"];
    d.forEach(function (v) {
        let li = document.createElement("li");
        li.innerHTML = addItem(v["name"], v["msg"], v["date"]);
        if(id != v["name"])
            li.className = "me";
        list.appendChild(li);
    });
}
function addItem(name, msg, date) {
    let html = `
        <div>
            <a href="/acc/profile/${name}"><p>${name}</p></a>
            <p>${msg}</p>
            <p class="date">${date}</p>
        </div>
    `;
    return html;
}
sender.onclick = () => {
    if (input.value.length > 0) {
        $.ajax({
            url: `send/${id}`,
            data: {
                "msg": input.value
            },
            success: function (r) {
                input.value = "";
            }
        });
    }
}
window.setInterval(() => live(), 500);