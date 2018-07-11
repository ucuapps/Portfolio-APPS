// And this((

window.addEventListener("resize", function() {
    if (window.matchMedia("(min-width: 450px) and (max-width: 740px)").matches) {
        var proj_containers = document.getElementsByClassName('proj_container');
        for(var i = 0; i < proj_containers.length; i++){
            proj_containers[i].style.maxWidth = "440px";
        }
        var projects = ["project", "intern_project", "volunteer_project"];
        for(var k = 0; k < projects.length; k++){
            var proj = document.getElementsByClassName(projects[k]);
            for(var i = 0; i < proj.length; i++) {
                proj[i].style.width = "150px";
            }
            for(var i = 0; i < proj.length; i++) {
                if(i>=2){
                    proj[i].style.marginTop = "40px";
                }else{
                    proj[i].style.marginTop = "0px";
                }
            }
        }
        var techs = document.getElementsByClassName('proj_tech');
        for(var i = 0; i < techs.length; i++) {
            techs[i].style.width = "170px";
        }
    }
    if(window.matchMedia("(min-width: 740px)").matches){
        var proj_containers = document.getElementsByClassName('proj_container');
        for(var i = 0; i < proj_containers.length; i++){
            proj_containers[i].style.maxWidth = "720px";
        }
        var projects = ["project", "intern_project", "volunteer_project"];
        for(var k = 0; k < projects.length; k++) {
            var proj = document.getElementsByClassName(projects[k]);
            for(var i = 0; i < proj.length; i++) {
                proj[i].style.width = "180px";
            }
            for(var i = 0; i < proj.length; i++) {
                if(i>=3){
                    proj[i].style.marginTop = "40px";
                }else{
                    proj[i].style.marginTop = "0px";
                }
            }
        }
        var techs = document.getElementsByClassName('proj_tech');
        for(var i = 0; i < techs.length; i++) {
            techs[i].style.width = "200px";
        }
    }
});