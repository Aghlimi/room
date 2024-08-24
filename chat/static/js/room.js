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
        let dev = document.createElement("dev");
        let a = document.createElement("a");
        let p = document.createElement("p");
        let date = document.createElement("p");
        dev.appendChild(a);
        dev.appendChild(p);
        dev.appendChild(date);
        a.href = `/acc/profile/${v["name"]}`;
        a.textContent = v["name"];
        p.textContent = v["msg"];
        date.textContent = v["date"];
        li.appendChild(dev);
        date.className = "date";
        li.onmouseover = function(){
            date.style.display = "block";
        }
        li.onmouseleave = function(){
            date.style.display = "none";
        }
        if (id != v["name"])
            li.className = "me";
        list.appendChild(li);

    });
    // document.head.appendChild(document.querySelector("link"));
    console.log(0);
    
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
