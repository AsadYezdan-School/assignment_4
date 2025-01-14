$(document).ready(function() {
    $('textarea').on('keyup keypress', function() {
        $(this).height(0);
        $(this).height(this.scrollHeight);
    });
});
let jsonBoxInput = document.getElementById('jsonBox');
let jsonInput = document.getElementById('json');
jsonBoxInput.addEventListener('focus',checkInput)
jsonInput.addEventListener('focus',checkInput)
function checkInput() {
    let submitButton = document.getElementById('submit_button');
    submitButton.style.opacity=0.5;
    submitButton.disabled = true;
    submitButton.style.cursor='not-allowed';
    
}
async function validateJSON(event) {
    event.preventDefault();
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const jsonBox = document.getElementById('json');
    let submitButton = document.getElementById('submit_button');
    
    try {
        const list = JSON.parse(jsonBox.value);  // Parse the input to ensure it's valid JSON
        console.log(list);
        let baseUrl = window.location.origin
        let redirect = baseUrl + "/books/bulkAdd/validateJSON/";
        console.log(redirect);
        const rawJSON = await fetch(redirect, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body:JSON.stringify(list)
        });

        const response = await rawJSON;
        if (response.ok) {
            console.log("Valid");
            jsonBox.style.backgroundColor = 'green';
            submitButton.disabled=false;
            submitButton.style.opacity=1;
        } else {
            console.log("Record couldn't be updated");
            jsonBox.style.backgroundColor = 'red';
        }
    } catch (error) {
        console.error("Invalid JSON:", error);
        jsonBox.style.backgroundColor = 'red';
    }
}

async function addFromJSON(event){
    event.preventDefault();
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let submitButton = document.getElementById('submit_button');
    const jsonBox = document.getElementById('json');
    
    try {
        const list = JSON.parse(jsonBox.value);  // Parse the input to ensure it's valid JSON
        console.log(list);
        let baseUrl = window.location.origin
        let redirect = baseUrl + "/books/bulkAdd/addFromJSON/";
        console.log(redirect);
        const rawJSON = await fetch(redirect, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body:JSON.stringify(list)
        });

        const response = await rawJSON;
        if (response.ok) {
            console.log("Valid");
            submitButton.style.backgroundColor = 'green';
            alert("Books Added Sucessfully")
        } else {
            submitButton.style.backgroundColor = 'red';
            alert("Books couldnt be added")
        }
    } catch (error) {
        console.error("Invalid JSON:", error);
        jsonBox.style.backgroundColor = 'red';
    }

}