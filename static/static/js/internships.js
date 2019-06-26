function mark_modals() {
    var modals = document.getElementsByClassName("modal");
    var desc_parents = document.querySelectorAll('[data-toggle="modal"]');
    var modal_titles = document.getElementsByClassName("modal-title");
    for (let i = 0; i < modals.length; i++) {
        modals[i].id = "intern_desc_modal_" + i;
        modals[i].setAttribute('aria-labelledby',"intern_modal_title_" + i);
        desc_parents[i].setAttribute('data-target',"#intern_desc_modal_" + i);
        modal_titles[i].id = "intern_modal_title_" + i;
    }            
}