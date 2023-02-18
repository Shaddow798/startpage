alert("Hello")

// start writing the scirpt to change the search engine
localStorage.setItem("search", "google");
var search = localStorage.getItem("search");

if (search == "duckduckgo") {
    pass
}
else if (search == "google") {
    document.getElementById("searchbar").action = "https://www.google.com/search?q="; //Will set it
    document.getElementsByClass('form-control').placeholder='new text for fname';
}
