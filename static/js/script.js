// Initialization of the side nave and placed it on the right side
//document.addEventListener('DOMContentLoaded', function() {
//  var sidenavs = document.querySelectorAll(".sidenav");
//    var sidenavsInstances = M.Sidenav.init(sidenavs, {edge: "right"});
//  });

  document.addEventListener('DOMContentLoaded', function() {
    var slinder = document.querySelectorAll('.slider');
    var instances = M.Slider.init(slinder);
  });

//  document.addEventListener('DOMContentLoaded', function() {
//    var elems = document.querySelectorAll('select');
//   var instances = M.FormSelect.init(elems);
//  });

 document.addEventListener('DOMContentLoaded', function () {
     let sidenavs = document.querySelectorAll(".sidenav");
     let sidenavsInstance = M.Sidenav.init(sidenavs, {edge: "right"});
     let selects = document.querySelectorAll("select");
     let selectsInstance = M.FormSelect.init(selects);

     validateMaterializeSelect();
     function validateMaterializeSelect() {
         let classValid = "border-bottom: 1px solid #4caf50; box-shadow: 0 1px 0 0 #4caf50;";
         let classInvalid = "border-bottom: 1px solid #f44336; box-shadow: 0 1px 0 0 #f44336;";
         let selectValidate = document.querySelector("select.validate");
         let selectWrapperInput = document.querySelector(".select-wrapper input.select-dropdown");
         if (selectValidate.hasAttribute("required")) {
             selectValidate.style.cssText = "display: block; height: 0; padding: 0; width: 0; position: absolute;";
         }
         selectWrapperInput.addEventListener("focusin", (e) => {
             e.target.parentNode.addEventListener("change", () => {
                 ulSelectOptions = e.target.parentNode.childNodes[1].childNodes;
                 for (let i = 0; i < ulSelectOptions.length; i++) {
                     if (ulSelectOptions[i].className == "selected" && ulSelectOptions[i].hasAttribute != "disabled") {
                         e.target.style.cssText = classValid;
                     }
                 }
             });
         });
         selectWrapperInput.addEventListener("click", (e) => {
            ulSelectOptions = e.target.parentNode.childNodes[1].childNodes;
             for (let i = 0; i < ulSelectOptions.length; i++) {
                 if (ulSelectOptions[i].className == "selected" && ulSelectOptions[i].hasAttribute != "disabled" && ulSelectOptions[i].style.backgroundColor == "rgba(0, 0, 0, 0.03)") {
                     e.target.style.cssText = classValid;
                 } else {
                     e.target.addEventListener("focusout", () => {
                         if (e.target.parentNode.childNodes[3].hasAttribute("required")) {
                             if (e.target.style.borderBottom != "1px solid rgb(76, 175, 80)") {
                                 e.target.style.cssText = classInvalid;
                             }
                         }
                     });
                 }
             }
         });
     }
 });