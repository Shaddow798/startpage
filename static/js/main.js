// This script controls the searchbox on the website.

//var backgroundcolor = localStorage.getItem("")
//var backgroundcolor = localStorage.getItem("colour");
//console.log(backgroundcolor);
document.getElementsByTagName('body')[0].style = 'background: #222;'; 
//const body = document.querySelector("body");
//body.style.background = "#44499";
//Manual overide for setting the search engine
//localStorage.setItem("search", "google");
var search = localStorage.getItem("search");

if (search == "duckduckgo") {
    document.getElementById("searchbar").action = "https://duckduckgo.com/?q="; //Will set it
    document.getElementById("searchtext").placeholder = "Search With DuckDuckgo."
}
else if (search == "google") {
    document.getElementById("searchbar").action = "https://www.google.com/search?q="; //Will set it
    document.getElementById("searchtext").placeholder = "Search With Google."
}
else if (search == "yahoo") {
    document.getElementById("searchbar").action = "https://www.search.yahoo.com/search?p="; //Will set it
    document.getElementById("searchtext").placeholder = "Search With Yahoo."
}
else if (search == "bing") {
    document.getElementById("searchbar").action = "https://www.bing.com/search?q="; //Will set it
    document.getElementById("searchtext").placeholder = "Search With Bing."
}
