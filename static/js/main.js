// This script controls the startpage on the site.

document.getElementById("searchtext").focus();


fontcolour = localStorage.getItem("font-colour")
document.getElementsByTagName('body')[0].style = 'color: ' + fontcolour;


// Set the background colour
// backgroundcolour = localStorage.getItem("colour")
// document.getElementsByTagName('body')[0].style = 'background: ' + backgroundcolour;

// document.getElementsByTagName('body')[0].style = 'background-image: {{ url_for('static', filename='images/proxmox.png') }}'
// document.getElementsByTagName('body')[0].style = 'background-image: /images/proxmox.png';


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
