const form = document.getElementById('form');
const password1El = document.getElementById('password1');
const password2El = document.getElementById('password2');
const messageContainer = document.getElementById('message');

let isValid = false;

function validateForm() {
    //Using Constraint API
    isValid = form.checkValidity();
    console.log(isValid);
    //Style main message for an error
    message.textContent = 'Please fill out all fields';
    message.style.color = 'red';
    messageContainer.style.borderColor = 'red'; //not working
}

function processFormData(e) {
    e.preventDefault();
    validateForm();
}

//Event Listner
form.addEventListener('submit', processFormData);