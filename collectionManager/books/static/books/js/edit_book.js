//page settings
//set up listeners to lock submit anytime the fields are being changed
let titleInput = document.getElementById('full_title');
let isbnInput = document.getElementById('isbn');
let orig_titleInput = document.getElementById('original_title');
let isbn13_Input = document.getElementById('isbn13');
titleInput.addEventListener('focus', checkInput);
isbnInput.addEventListener('focus', checkInput);
orig_titleInput.addEventListener('focus',checkInput)
isbn13_Input.addEventListener('focus',checkInput)

// AJAX server to get validity of a title to check if what we're adding is a duplicate or not 
async function validateTitle(event){
    event.preventDefault();
    const book_id = document.getElementById('book_id').value;
    const title = document.getElementById('full_title').value;
    const titleDiv = document.getElementById('full_title');
    const orig_titleDiv = document.getElementById('original_title')
    const encodedTitle = encodeURIComponent(title);
    console.log(`checking title : ${title}`);
    try{
        // Ask the django view called validate-title mapped to the url validate-title to check if the title is actually new
        baseUrl =window.location.origin;
        validateUrl = baseUrl +'/'+ `books/validate-title-update/${encodedTitle}/${book_id}/`;
        console.log(validateUrl);
        const response = await fetch(validateUrl,
            {
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
            }
        );
        if (!response.ok) {
            throw new Error('Failed to validate input');
        }
        
        const data = await response.json();

        if(data.valid){
            changeDivStyleGreen(titleDiv)
            changeDivStyleGreen(orig_titleDiv)
            return true
        } else {
            changeDivStyleRed(titleDiv)
            changeDivStyleRed(orig_titleDiv)
            return false
        }
    } catch(error) {
        changeDivStyleYellow(titleDiv)
        changeDivStyleYellow(orig_titleDiv)
        orig_titleDiv
        console.error('Fetch error: ', error.message);
        console.error('Error stack: ', error.stack); 
        if (error.response) {
          console.error('Response:', error.response); }
        console.error('Error:', error);
    }
}

async function validateISBN(event){
    event.preventDefault();
    const book_id = document.getElementById('book_id').value;
    const isbn = document.getElementById('isbn').value;
    const isbnDiv = document.getElementById('isbn');
    const encodedIsbn = encodeURIComponent(isbn);
    console.log(`checking isbn : ${isbn}`);
    try{
        // Ask the django view called validate-title mapped to the url validate-title to check if the title is actually new
        baseUrl =window.location.origin;
        validateUrl = baseUrl +'/'+ `books/validate-isbn-update/${encodedIsbn}/${book_id}/`;
        console.log(validateUrl);
        const response = await fetch(validateUrl,
            {
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
            }
        );
        if (!response.ok) {
            throw new Error('Failed to validate input');
        }
        
        const data = await response.json();

        if(data.valid){
            changeDivStyleGreen(isbnDiv)
            return true
        } else {
            changeDivStyleRed(isbnDiv)
            return false
        }
    } catch(error) {
        changeDivStyleYellow(isbnDiv)
        console.error('Fetch error: ', error.message);
        console.error('Error stack: ', error.stack); 
        if (error.response) {
          console.error('Response:', error.response); }
        console.error('Error:', error);
    }
}
async function validateISBN(event){
    event.preventDefault();
    const book_id = document.getElementById('book_id').value;
    const isbn = document.getElementById('isbn').value;
    const isbnDiv = document.getElementById('isbn');
    const encodedIsbn = encodeURIComponent(isbn);
    console.log(`checking isbn : ${isbn}`);
    try{
        // Ask the django view called validate-title mapped to the url validate-title to check if the title is actually new
        baseUrl =window.location.origin;
        validateUrl = baseUrl +'/'+ `books/validate-isbn-update/${encodedIsbn}/${book_id}/`;
        console.log(validateUrl);
        const response = await fetch(validateUrl,
            {
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
            }
        );
        if (!response.ok) {
            throw new Error('Failed to validate input');
        }
        
        const data = await response.json();

        if(data.valid){
            changeDivStyleGreen(isbnDiv)
            return true
        } else {
            changeDivStyleRed(isbnDiv)
            return false
        }
    } catch(error) {
        changeDivStyleYellow(isbnDiv)
        console.error('Fetch error: ', error.message);
        console.error('Error stack: ', error.stack); 
        if (error.response) {
          console.error('Response:', error.response); }
        console.error('Error:', error);
    }
}

async function validateISBN13(event){
    event.preventDefault();
    const book_id = document.getElementById('book_id').value;
    const isbn13 = document.getElementById('isbn13').value;
    const isbn13Div = document.getElementById('isbn13');
    const encodedIsbn13 = encodeURIComponent(isbn13);
    console.log(`checking isbn13 : ${isbn13}`);
    try{
        // Ask the django view called validate-title mapped to the url validate-title to check if the title is actually new
        baseUrl =window.location.origin;
        validateUrl = baseUrl +'/'+ `books/validate-isbn13-update/${encodedIsbn13}/${book_id}/`;
        console.log(validateUrl);
        const response = await fetch(validateUrl,
            {
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
            }
        );
        if (!response.ok) {
            throw new Error('Failed to validate input');
        }
        
        const data = await response.json();

        if(data.valid){
            changeDivStyleGreen(isbn13Div)
            return true
        } else {
            changeDivStyleRed(isbn13Div)
            return false
        }
    } catch(error) {
        changeDivStyleYellow(isbn13Div)
        console.error('Fetch error: ', error.message);
        console.error('Error stack: ', error.stack); 
        if (error.response) {
          console.error('Response:', error.response); }
        console.error('Error:', error);
    }
}
//lock the submit button when there is somehting being typed in the forms
function checkInput() {
    let submitButton = document.getElementById('submit_button');

    // If the input is empty, disable the button
    submitButton.disabled = true;
    submitButton.style.opacity=0.5;

    // If the input is not empty, enable the button
    submitButton.disabled = false;

    //set cursor to not allowed
    submitButton.style.cursor='not-allowed';
    
}

async function validateInputs(event){
    title_valid = await validateTitle(event);
    isbn_valid = await validateISBN(event);
    isbn13_valid = await validateISBN13(event);
    if(isbn_valid && title_valid && isbn13_valid){
        // make sumbit button opaque and unlock it if both fields are valid
        let submitter = document.getElementById('submit_button');
        submitter.style.opacity=1;
        submitter.disabled = false;
        submitter.style.cursor= 'pointer';
    }else{
        let submitter = document.getElementById('submit_button');
        submitter.style.opacity = 0.5;
        submitter.disabled=true;
    }
}

async function updateRecord(event){
    event.preventDefault();
    console.log("made it to the update record method")
    /* console.log("made it to the JS method")
    event.preventDefault();
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    console.log("submit button was pushed")
    let title = document.getElementById('full_title').value;
    let isbn = document.getElementById('isbn').value;
    let authors = document.getElementById('authors').value;
    let publication_year = document.getElementById('publication_year').value;
    let url = document.getElementById('url').value;
    let language_code = document.getElementById('lang_code').value;
    let avg_rating = 0.0;
    let rating_count = 0;
    let formDictionary = {
        "goodreads_book_id":"",
        "best_book_id":"",
        "work_id":"",
        "books_count":"",
        "isbn":isbn,
        "isbn13":isbn,
        "authors":authors,
        "original_publication_year":publication_year,
        "original_title":title,
        "title":title,
        "language_code":language_code,
        "average_rating": avg_rating,
        "ratings_count":rating_count,
        "work_ratings_count":rating_count,
        "work_text_reviews_count":rating_count,
        "ratings_1":rating_count,
        "ratings_2":rating_count,
        "ratings_3":rating_count,
        "ratings_4":rating_count,
        "ratings_5":rating_count,
        "image_url":url,
        "small_image_url":url

    }
    console.log("made the dictionary")
    let formData = new URLSearchParams(formDictionary).toString();
    let baseUrl = window.location.origin;
    let redirectUrl = baseUrl + '/books/add-book/add-record/';
    console.log(`redirecting to ${redirectUrl} to add book`)
    try{
        const response = await fetch(redirectUrl,{
            method:'POST',
            headers:{'Content-Type': 'application/x-www-form-urlencoded', 'X-CSRFToken':csrfToken},
            body: formData
        });
        if (response.ok){
            console.log("Book added");
            alert("Book was successfully added");
        }else{
            console.log("Book couldnt be added");
        }
    }catch(error) {
        console.error(error);
    } */
}
console.log("JS Script loaded!")

function changeDivStyleRed(inputDiv) {
// Change the div's style dynamically when clicked
inputDiv.style.backgroundColor = '#f8d7da';  // Light red background
inputDiv.style.borderColor = '#dc3545';      // Dark red border
inputDiv.style.color = '#721c24';             // Dark red text
}
function changeDivStyleGreen(inputDiv) {
inputDiv.style.backgroundColor = '#d4edda'; // Light green background
inputDiv.style.borderColor = '#28a745';      // Dark green border
inputDiv.style.color = '#155724';             // Dark green text
}
function changeDivStyleYellow(inputDiv) {
inputDiv.style.backgroundColor = '#fff3cd'; // Light yellow background
inputDiv.style.borderColor = '#ffc107';     // Dark yellow border
inputDiv.style.color = '#856404';            // Dark yellow text
}