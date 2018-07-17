function openNav() {
    document.getElementById("pop_menu").style.width = "200px";
    document.getElementById("overlay").style.visibility = "visible";
    document.getElementById("overlay").style.opacity = .7;
}

function closeNav() {
    document.getElementById("pop_menu").style.width = "0";
    document.getElementById("overlay").style.opacity = 0;
    document.getElementById("overlay").style.visibility = "hidden";
}

function popup_func() {
    var popup = document.getElementsByClassName("popup")[0];
    var popup_request = document.getElementsByClassName("popup")[1];
    popup.style.display = "flex";
    popup_request.style.display = "none";
}
function popup_request_func() {
    var popup = document.getElementsByClassName("popup")[0];
    var popup_request = document.getElementsByClassName("popup")[1];
    popup.style.display = "none";
    popup_request.style.display = "flex";
}

document.onclick = function(e){
    var popup = document.getElementById("popup");
    for(var i = 0; i < popup.length; i++){
        if(e.target.className !== "avatar" && e.target.id !== "popup"){
            popup.style.display = 'none';
        }
    }
};