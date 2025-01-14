async function addToRead(event) {
    console.log("made it to the JS method");
    event.preventDefault();

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const id = parseInt(document.getElementById('book_id').value);
    const  userID = parseInt(document.getElementById('user_id').value);  // Convert to integer

    let userDiv = document.getElementById('user_id');

    let list = [{'user_id': userID, 'book_id': id,}];  
    try {
        console.log(list);
        let baseUrl = window.location.origin;
        let redirect = baseUrl + "/books/submit-to-read/";
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
            alert("Book added to list sucessfully");
        } else {
            userDiv.style.backgroundColor = 'red';
            alert("Book couldnt be added, invalid user id, must be < 54432, for other errors check developer console");
        }
    } catch (error) {
        console.error("Invalid JSON:", error);
    }
}





