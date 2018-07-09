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
    var popup = document.getElementById("popup");
    popup.style.display = "flex";
}

document.onclick = function(e){
    var popup = document.getElementById("popup");
    if(e.target.className !== "avatar" && e.target.id !== "popup"){
        popup.style.display = 'none';
    }
};