function setsearch() {
    search = document.getElementById("searchengine"),
    searchvalue = search.value;
    localStorage.setItem("search", searchvalue);
    alert("Your setting has been applied sucsesfully")
}



// var search = localStorage.getItem("search");