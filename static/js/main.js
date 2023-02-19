// This script controls the searchbox on the website.

//var backgroundcolor = localStorage.getItem("")
var backgroundcolor = '#4443';
//document.getElementsByClassName("content-div").style = 'background: red;'
document.getElementsByTagName('body')[0].style = 'background: #333;'; 

//Manual overide for setting the search engine
//localStorage.setItem("search", "google");
var search = localStorage.getItem("search");

if (search == "duckduckgo") {
    document.getElementById("searchbar").action = "https://duckduckgo.com/?q="; //Will set it
    document.getElementsByClass('form-control').placeholder='new text for fname';
}
else if (search == "google") {
    document.getElementById("searchbar").action = "https://www.google.com/search?q="; //Will set it
    document.getElementsByClass('form-control').placeholder='new text for fname';
}
else if (search == "yahoo") {
    document.getElementById("searchbar").action = "https://www.search.yahoo.com/search?p="; //Will set it
//    document.getElementsByClass('form-control').placeholder='new text for fname';

}
else if (search == "bing") {
    document.getElementById("searchbar").action = "https://www.bing.com/search?q="; //Will set it
//    document.getElementsByClass('form-control').placeholder='new text for fname';
}
