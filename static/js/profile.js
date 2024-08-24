let username = document.querySelector("h1").innerText;
$.ajax({
    url:"/acc/get_data/"+username,
    success:function(results){
        if(results.success){
            document.querySelector("img").src = results.image;
            document.querySelector("h4").innerText = results.name;
            document.querySelector("#date").innerText = results.date;
            document.querySelector("#sex").innerText = results.sex;
            document.querySelector("#email").innerText = results.email;
        }else{
        document.querySelector("div").innerHTML = "no user"}
    }
})