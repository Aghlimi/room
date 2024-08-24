
function like(button, url) {
    $.ajax({
        url: url,
        success: function (result) {
            button.innerHTML = "likes:" + result["like"];
        }
    });
}
let form = document.querySelector("form");
form.onsubmit = (e) => {
    e.preventDefault();
    if (document.querySelector("textarea").value != "" || document.querySelector("input[name=image]").value != "") {
        var data = new FormData(form);
        $.ajax({
            url: window.location.href,
            method: "POST",
            data: data,
            contentType: false,
            processData: false,
            success: function (r) {
                window.localStorage.setItem("tt", "ff")
                location.reload();

            }
        });
    }
}
