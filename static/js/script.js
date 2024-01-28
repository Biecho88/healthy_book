// Initialization of the side nave and placed it on the right side
document.addEventListener('DOMContentLoaded', function() {
    var sidenavs = document.querySelectorAll(".sidenav");
    var sidenavsInstances = M.Sidenav.init(sidenavs, {edge: "right"});
  });