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
  var search_query = document.querySelector('.search-box').value;
  console.log("Got the title its "+ search_query)
  var newUrl = '/books/search-results/' + search_query + '/';
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
async function addRating(event) {
    console.log("made it to the JS method");
    event.preventDefault();

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const id = parseInt(document.getElementById('book_id').value);
    const rating = parseInt(document.getElementById('rating').value);  // Convert to integer
    const  userID = parseInt(document.getElementById('user_id').value);  // Convert to integer

    let userDiv = document.getElementById('user_id');
    let ratingDiv = document.getElementById('rating');

    let list = [{'user_id': userID, 'book_id': id, 'rating': rating}];  // Ensure rating is an integer
    try {
        console.log(list);
        let baseUrl = window.location.origin;
        let redirect = baseUrl + "/books/submit-rating/";
        console.log(redirect);

        const rawJSON = await fetch(redirect, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(list)
        });

        const response = await rawJSON;
        if (response.ok) {
            console.log("Valid");
            userDiv.style.backgroundColor = 'green';
            ratingDiv.style.backgroundColor = 'green';
            alert("Rating added successfully, and relevant fields updated");
        } else {
            userDiv.style.backgroundColor = 'red';
            ratingDiv.style.backgroundColor = 'red';
            alert("Ratings couldn't be added");
        }
    } catch (error) {
        console.error("Invalid JSON:", error);
    }
}





