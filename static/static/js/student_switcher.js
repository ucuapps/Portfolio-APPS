// Fix this gauno code as soon as possible

function hard() {
    var proj = document.getElementById('projcont');
    var hobbies = document.getElementById('hobbies');
    var hard = document.getElementById('hard');

    proj.style.display = "none";
    hobbies.style.display = "none";
    hard.style.display = "flex";
    document.getElementsByClassName('proj_sw')[0].style.color = "rgb(101,57,152)";
    document.getElementsByClassName('switch')[0].style.borderBottom = "2px solid rgb(101,57,152)";
    document.getElementsByClassName('proj_sw')[1].style.color = "rgb(68,68,68)";
    document.getElementsByClassName('switch')[1].style.borderBottom = "none";
    document.getElementsByClassName('switch')[2].style.color = "rgb(68,68,68)";
    document.getElementsByClassName('proj_sw')[2].style.borderBottom = "none";

}

function proj() {
    var proj = document.getElementById('projcont');
    var hobbies = document.getElementById('hobbies');
    var hard = document.getElementById('hard');

    hard.style.display = "none";
    hobbies.style.display = "none";
    proj.style.display = "flex";
    document.getElementsByClassName('proj_sw')[1].style.color = "rgb(101,57,152)";
    document.getElementsByClassName('switch')[1].style.borderBottom = "2px solid rgb(101,57,152)";
    document.getElementsByClassName('proj_sw')[0].style.color = "rgb(68,68,68)";
    document.getElementsByClassName('switch')[0].style.borderBottom = "none";
    document.getElementsByClassName('proj_sw')[2].style.color = "rgb(68,68,68)";
    document.getElementsByClassName('switch')[2].style.borderBottom = "none";
}

function hobbies() {
    var proj = document.getElementById('projcont');
    var hobbies = document.getElementById('hobbies');
    var hard = document.getElementById('hard');

    proj.style.display = "none";
    hard.style.display = "none";
    hobbies.style.display = "flex";
    document.getElementsByClassName('proj_sw')[2].style.color = "rgb(101,57,152)";
    document.getElementsByClassName('switch')[2].style.borderBottom = "2px solid rgb(101,57,152)";
    document.getElementsByClassName('proj_sw')[1].style.color = "rgb(68,68,68)";
    document.getElementsByClassName('switch')[1].style.borderBottom = "none";
    document.getElementsByClassName('proj_sw')[0].style.color = "rgb(68,68,68)";
    document.getElementsByClassName('switch')[0].style.borderBottom = "none";
}

function internship(){
    var proj = document.getElementById('proj');
    var intern = document.getElementById('intern');
    var volunteer = document.getElementById('volunteer');

    proj.style.display = "none";
    volunteer.style.display = "none";
    intern.style.display = "flex";

    document.getElementsByClassName('proj_sw')[4].style.color = "rgb(101,57,152)";
    document.getElementsByClassName('switch')[4].style.borderBottom = "2px solid rgb(101,57,152)";
    document.getElementsByClassName('proj_sw')[3].style.color = "rgb(68,68,68)";
    document.getElementsByClassName('switch')[3].style.borderBottom = "none";
    document.getElementsByClassName('proj_sw')[5].style.color = "rgb(68,68,68)";
    document.getElementsByClassName('switch')[5].style.borderBottom = "none";
}

function volunteer(){
    var proj = document.getElementById('proj');
    var intern = document.getElementById('intern');
    var volunteer = document.getElementById('volunteer');

    proj.style.display = "none";
    volunteer.style.display = "flex";
    intern.style.display = "none";

    document.getElementsByClassName('proj_sw')[5].style.color = "rgb(101,57,152)";
    document.getElementsByClassName('switch')[5].style.borderBottom = "2px solid rgb(101,57,152)";
    document.getElementsByClassName('proj_sw')[3].style.color = "rgb(68,68,68)";
    document.getElementsByClassName('switch')[3].style.borderBottom = "none";
    document.getElementsByClassName('proj_sw')[4].style.color = "rgb(68,68,68)";
    document.getElementsByClassName('switch')[4].style.borderBottom = "none";
}

function project(){
    var proj = document.getElementById('proj');
    var intern = document.getElementById('intern');
    var volunteer = document.getElementById('volunteer');

    proj.style.display = "flex";
    volunteer.style.display = "none";
    intern.style.display = "none";

    document.getElementsByClassName('proj_sw')[3].style.color = "rgb(101,57,152)";
    document.getElementsByClassName('switch')[3].style.borderBottom = "2px solid rgb(101,57,152)";
    document.getElementsByClassName('proj_sw')[5].style.color = "rgb(68,68,68)";
    document.getElementsByClassName('switch')[5].style.borderBottom = "none";
    document.getElementsByClassName('proj_sw')[4].style.color = "rgb(68,68,68)";
    document.getElementsByClassName('switch')[4].style.borderBottom = "none";
}

function popup() {
    document.getElementsByClassName('popup')[0].style.display = "flex";
}

function close() {
    document.getElementsByClassName('popup')[0].style.display = "none";
}