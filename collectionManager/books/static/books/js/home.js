function submitQuery(event){
    event.preventDefault();
    var search_query = document.querySelector('.search-box').value;
    console.log("Got the title its "+ search_query)
    window.location.href = `search-results/${search_query}`;
    
}