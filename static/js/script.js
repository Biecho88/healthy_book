
 document.addEventListener('DOMContentLoaded', function () {
     let sidenavs = document.querySelectorAll(".sidenav");
     let sidenavsInstance = M.Sidenav.init(sidenavs, {edge: "right"});
     let selects = document.querySelectorAll("select");
     let selectsInstance = M.FormSelect.init(selects);
     let slinder = document.querySelectorAll('.slider');
     let instances = M.Slider.init(slinder);

 });