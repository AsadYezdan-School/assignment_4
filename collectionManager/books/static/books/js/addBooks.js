// AJAX server to get validity of a title to check if what we're adding is a duplicate or not 
async function validateTitle(event){
    event.preventDefault();
    const title = document.getElementById('full_title').value;
    const titleDiv = document.getElementById('full_title');
    const encodedTitle = encodeURIComponent(title);
    console.log(`made it inside the JS method, title : ${title}`);
    try{
        // Ask the django view called validate-title mapped to the url validate-title to check if the title is actually new
        console.log("Made it inside the fetch");
        baseUrl =window.location.origin;
        validateUrl = baseUrl +'/'+ `books/validate-title/${encodedTitle}`;
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
            titleDiv.textContent="This title isnt already used ";
            titleDiv.style.color = 'green';
            console.log("We coolin")
        } else {
            titleDiv.textContent='A book with this title already exists in the DB! Check again or add some information to the title to make it unique';
            titleDiv.style.color = 'red';
            console.log("We NOT cooling")
        }
    } catch(error) {
        titleDiv.textContent = 'Error validating input. Try again later';
        titleDiv.style.color = 'orange';
        console.error('Fetch error: ', error.message);
        console.error('Error stack: ', error.stack); 
        if (error.response) {
          console.error('Response:', error.response); }
        console.error('Error:', error);
    }
}

async function validateISBN(event){
    event.preventDefault();
    const isbn = document.getElementById('isbn').value;
    const titleDiv = document.getElementById('isbn');
    const encodedIsbn = encodeURIComponent(isbn);
    console.log(`made it inside the JS method, isbn : ${isbn}`);
    try{
        // Ask the django view called validate-title mapped to the url validate-title to check if the title is actually new
        console.log("Made it inside the fetch");
        baseUrl =window.location.origin;
        validateUrl = baseUrl +'/'+ `books/validate-isbn/${encodedIsbn}`;
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
            titleDiv.textContent="This isbn isnt already used";
            titleDiv.style.color = 'green';
            console.log("We coolin")
        } else {
            titleDiv.textContent='A book with this isbn already exists in the DB! Check again or add some information to the title to make it unique';
            titleDiv.style.color = 'red';
            console.log("We NOT cooling")
        }
    } catch(error) {
        titleDiv.textContent = 'Error validating input. Try again later';
        titleDiv.style.color = 'orange';
        console.error('Fetch error: ', error.message);
        console.error('Error stack: ', error.stack); 
        if (error.response) {
          console.error('Response:', error.response); }
        console.error('Error:', error);
    }

}

async function validateInputs(event){
    isbn_valid = validateISBN(event)
    title_valid = validateTitle(event)
}