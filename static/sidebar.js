// Expand Navbar

function myFunction(x) {
  document.getElementById("openbutton").onclick= function() {openNav()};
  document.getElementById("closebutton").onclick= function() {closeNav()};
    if (x.matches) { // If media query matches
      document.getElementById("mySidebar").style.width = "0";
      function openNav() {
           document.getElementById("mySidebar").style.width = "200px";
        }
      function closeNav() {
          document.getElementById("mySidebar").style.width = "0";
        }
    } 
    else {
      document.getElementById("mySidebar").style.width = "200px";    
    }
}

var x = window.matchMedia("(max-width: 880px)")
myFunction(x) // Call listener function at run time
x.addEventListener("change", myFunction)// Attach listener function on state changes



