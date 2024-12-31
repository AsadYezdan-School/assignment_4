function validateSearch() {
    var searchInput = document.getElementById("search").value;
    if (searchInput.trim() === "") {
      alert("Please enter a search term.");
      return false;  // Prevent form submission
    }
    return true;  // Allow form submission
  }