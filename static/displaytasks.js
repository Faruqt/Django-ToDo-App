function displayCurrentTasks() {
    var x= document.getElementById("currentTasks");
    var y= document.getElementById("overdueTasks");
    var z1= document.getElementById("currentTasksButton");
    var z2= document.getElementById("overDueTasksButton");

    z1.disabled = "true";
    z1.style.backgroundColor= "whitesmoke";
    z2.removeAttribute("disabled");
    z2.style.backgroundColor= "#323647";

    if (x.style.display === "none") {
      x.style.display = "block";
      y.style.display = "none"
    }
    else if (x.style.display === "block") {
      x.style.display = "none"; 
      y.style.display = "block"
    }
    else {
      x.style.display = "block";
      y.style.display = "none"
    }
  }
  
/* display team login form*/
function displayOverDueTasks() {
    var x= document.getElementById("overdueTasks");
    var y= document.getElementById("currentTasks");
    var z1= document.getElementById("overDueTasksButton");
    var z2= document.getElementById("currentTasksButton");

    z1.disabled = "true";
    z1.style.backgroundColor= "whitesmoke";
    z2.removeAttribute("disabled");
    z2.style.backgroundColor= "#323647";
    
    if (x.style.display === "none") {
      x.style.display = "block";
      y.style.display = "none"
    }
    else if (x.style.display === "block") {
      x.style.display = "none"; 
      y.style.display = "block"
    }
    else {
      x.style.display = "block";
      y.style.display = "none"
    }
  }

