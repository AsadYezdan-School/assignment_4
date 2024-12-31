async function validateTitle(){
    const title = document.getElementById('full_title').value;
    const titleDiv = document.getElementById('full_title');
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    try{
        // Ask the django view called validate-title mapped to the url validate-title to check if the title is actually new
        console.log("Made it inside the fetch")
        const response = await fetch('/validate-title/?validate='+ title,
            {
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
            }
        );
        if (!response.ok) {
            throw new Error('Failed to validate input');
        }
        
        const data = await response.json;

        if(data.valid){
            titleDiv.textContent("This title isnt already used ");
            titleDiv.style.color = 'green';
            console.log("We coolin")
        } else {
            titleDiv.textContent('A book with this title already exists in the DB! Check again or add some information to the title to make it unique');
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

async function validateISBN(){

}