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