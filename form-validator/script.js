const form = document.getElementById('form');
const password1El = document.getElementById('password1');
const password2El = document.getElementById('password2');
const messageContainer = document.getElementById('message');

function processFormData(e) {
    console.log(e);
}

//Event Listner
form.addEventListener('submit', processFormData);