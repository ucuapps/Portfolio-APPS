function teacher_info() {
    var proj = document.getElementById('projcont');
    var hard = document.getElementById('hard');

    proj.style.display = "none";
    hard.style.display = "flex";
    document.getElementsByClassName('proj_sw')[0].style.color = "rgb(101,57,152)";
    document.getElementsByClassName('switch')[0].style.borderBottom = "2px solid rgb(101,57,152)";
    document.getElementsByClassName('proj_sw')[1].style.color = "rgb(68,68,68)";
    document.getElementsByClassName('switch')[1].style.borderBottom = "none";

}

function courses() {
    document.getElementsByClassName('student_info')[0].style.justifyContent = "center";
    var proj = document.getElementById('projcont');
    var hard = document.getElementById('hard');
    document.getElementsByClassName('switchers')[1].style.display = "none";

    hard.style.display = "none";
    proj.style.display = "flex";
    document.getElementsByClassName('proj_sw')[1].style.color = "rgb(101,57,152)";
    document.getElementsByClassName('switch')[1].style.borderBottom = "2px solid rgb(101,57,152)";
    document.getElementsByClassName('proj_sw')[0].style.color = "rgb(68,68,68)";
    document.getElementsByClassName('switch')[0].style.borderBottom = "none";
}