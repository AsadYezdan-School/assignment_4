function validateSearch() {
    var searchInput = document.getElementById("search").value;
    if (searchInput.trim() === "") {
      alert("Please enter a search term.");
      return false;  // Prevent form submission
    }
    return true;  // Allow form submission
  }
function submitQuery(event){
  event.preventDefault();
  var user_id = document.querySelector('.search-box').value;
  console.log("Got the user_id "+ user_id)
  var newUrl = '/books/view-to-read/' + user_id + '/';
  window.location.href = newUrl;

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


