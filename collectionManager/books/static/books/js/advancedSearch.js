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
document.addEventListener("DOMContentLoaded", function() {
    // Select all options buttons
    var optionsButtons = document.querySelectorAll('.ellipsis');
    console.log("made it to selecting all the options buttons")
  
    optionsButtons.forEach(function(button) {
      button.addEventListener('click', function(event) {
        console.log("we have a listner on each button")
        // Get the book ID from the data attribute
        var bookId = button.getAttribute('data-book-id');
        
        // Hide any currently open popups
        var allPopups = document.querySelectorAll('.options_menu');
        allPopups.forEach(function(popup) {
          popup.style.display = 'none';
        });
  
        // Get the specific popup for this book and toggle it
        var popup = document.getElementById('popup-' + bookId);
        popup.style.display = (popup.style.display === 'block') ? 'none' : 'block';
      });
    });
  });
