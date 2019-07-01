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
    var popup = document.getElementsByClassName("popup");
    if(e.target.className !== "request" && e.target.className !== "avatar" && e.target.className !== "popup"){
        console.log(popup.length);
        for(var i = 0; i < popup.length; i++){
            popup[i].style.display = 'none';
        }
    }
};