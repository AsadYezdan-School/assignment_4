//page settings
//set up listeners to lock submit anytime the fields are being changed
let titleInput = document.getElementById('title');
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
    const title = document.getElementById('title').value;
    const titleDiv = document.getElementById('title');
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
    
    event.preventDefault();
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    console.log("submit button was pushed")
    let book_id = document.getElementById('book_id').value  
    let goodreads_book_id = document.getElementById('goodreads_book_id').value ?? 0;
    goodreads_book_id = goodreads_book_id || 404;
    console.log("heres goodreads_book_id")
    console.log(goodreads_book_id)
    let best_book_id = document.getElementById('best_book_id').value || 404;
    best_book_id = best_book_id ?? 404;
    let work_id = document.getElementById('work_id').value || 404;
    work_id = work_id || 404;
    let books_count = document.getElementById('books_count').value;
    books_count = books_count ?? 0;
    let isbn = document.getElementById('isbn').value;
    let isbn13 = document.getElementById('isbn13').value;
    let authors = document.getElementById('authors').value;
    let original_publication_year = document.getElementById('original_publication_year').value;
    let original_title = document.getElementById('original_title').value;
    let title = document.getElementById('title').value;
    let language_code = document.getElementById('language_code').value;
    let average_rating= document.getElementById('average_rating').value;
    let ratings_count= document.getElementById('ratings_count').value;
    let work_ratings_count = document.getElementById('work_ratings_count').value;
    let work_text_reviews_count = document.getElementById('work_text_reviews_count').value;
    let ratings_1 = document.getElementById('ratings_1').value;
    let ratings_2 = document.getElementById('ratings_2').value;
    let ratings_3 = document.getElementById('ratings_3').value;
    let ratings_4 = document.getElementById('ratings_4').value;
    let ratings_5 = document.getElementById('ratings_5').value;
    let image_url = document.getElementById('image_url').value;
    let small_image_url = document.getElementById('small_image_url').value;

    let formDictionary = {
        "book_id":book_id,
        "goodreads_book_id":goodreads_book_id,
        "best_book_id":best_book_id,
        "work_id":work_id,
        "books_count":books_count,
        "isbn":isbn,
        "isbn13":isbn13,
        "authors":authors,
        "original_publication_year":original_publication_year,
        "original_title":original_title,
        "title":title,
        "language_code":language_code,
        "average_rating": average_rating,
        "ratings_count":ratings_count,
        "work_ratings_count":work_ratings_count,
        "work_text_reviews_count":work_text_reviews_count,
        "ratings_1":ratings_1,
        "ratings_2":ratings_2,
        "ratings_3":ratings_3,
        "ratings_4":ratings_4,
        "ratings_5":ratings_5,
        "image_url":image_url,
        "small_image_url":small_image_url
    }
    console.log("you are update to update with these values :")
    for (const key in formDictionary) {
        if (formDictionary.hasOwnProperty(key)) { // Ensures it is an own property
          console.log(`Key: ${key}, Value: ${formDictionary[key]}`);
        }
      }
    alert("Do you wanna continue")
    let formData = new URLSearchParams(formDictionary).toString();
    let baseUrl = window.location.origin;
    let redirectUrl = baseUrl + `/books/update-record/${book_id}`;
    console.log(`redirecting to ${redirectUrl} to add book`)
    let previousUrl = document.referrer;
    console.log(`will return to ${previousUrl}`)
    try{
        const response = await fetch(redirectUrl,{
            method:'POST',
            headers:{'Content-Type': 'application/x-www-form-urlencoded', 'X-CSRFToken':csrfToken},
            body: formData
        });
        if (response.ok){
            console.log("Record added");
            alert("Record was updated successfully");
            window.location.href = previousUrl; //recirect to where we were before the edit page opened
        }else{
            console.log("Record couldnt be updated");
            alert("Record couldnt be updated, see console logs in the developers console for details")
        }
    }catch(error) {
        console.error(error);
    } 
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