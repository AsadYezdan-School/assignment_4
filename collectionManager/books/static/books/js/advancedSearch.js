document.getElementById('fields_form').addEventListener('submit', function(event){

    title = document.getElementById('full_title').value;
    isbn = document.getElementById('isbn').value;
    authors = document.getElementById('authors').value;
    year_published = document.getElementById('publication_year').value;
    avg_rating = document.getElementById('avgRating').value;
    ratings_count = document.getElementById('ratingsCount').value;
    lang_code = document.getElementById('lang_code').value;

    if ( !title && !isbn && !authors && !year_published && !avg_rating && !ratings_count && !lang_code){
        event.preventDefault();
        alert("At least one field needs to have a value!")
    }

});

function toggle_menu(){
    var menu = document.getElementById("drop_down");
    menu.style.display = (menu.style.display === 'block') ? 'none' : 'block'; // toggle between showing the div and hiding it
}
