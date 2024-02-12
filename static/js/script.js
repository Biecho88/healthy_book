// Initialization of the side nave and placed it on the right side
document.addEventListener('DOMContentLoaded', function() {
    var sidenavs = document.querySelectorAll(".sidenav");
    var sidenavsInstances = M.Sidenav.init(sidenavs, {edge: "right"});
  });

  document.addEventListener('DOMContentLoaded', function() {
    var slinder = document.querySelectorAll('.slider');
    var instances = M.Slider.init(slinder);
  });

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
  });