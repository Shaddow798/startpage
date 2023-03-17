function setsearch() {
    search = document.getElementById("searchengine"),
    searchvalue = search.value;
    localStorage.setItem("search", searchvalue);
    alert("Your setting has been applied sucsesfully")
}

localStorage.setItem("backgroundtype", "solid")


function backgroundcolor() {
    color = document.getElementById("")
}




let colourpicker;
const defaultColor = "#000000";

window.addEventListener("load", startup, false);

function startup() {
    colourpicker = document.querySelector("#colourpicker");
    colourpicker.value = defaultColor;
    colourpicker.addEventListener("input", updateFirst, false);
    colourpicker.addEventListener("change", updateAll, false);
    colourpicker.select();
  }
  
  function updateFirst(event) {
    const body = document.querySelector("body");
    if (body) {
      body.style.background = event.target.value;
    }
  }
  
  function updateAll(event) {
    document.querySelectorAll("body").forEach((body) => {
      //body.style.background = event.target.value;
      localStorage.setItem("colour", event.target.value)
    });
  }
  


// var search = localStorage.getItem("search");