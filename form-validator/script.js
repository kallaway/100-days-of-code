const form = document.getElementById('form');
const password1El = document.getElementById('password1');
const password2El = document.getElementById('password2');
const messageContainer = document.getElementById('.message-container');
const message = document.getElementById('message');

let isValid = false;
let passwordsMatch = false;

function validateForm() {
    //Using Constraint API
    isValid = form.checkValidity();
    console.log(isValid);
    //Style main message for an error
    if (!isValid) {
        message.textContent = 'Please fill out all fields';
        message.style.color = 'red';
        messageContainer.style.borderColor = "red";
        //block return statement, that ends crawling the script
        return;
    }
    // Check to see if passwords match
    if (password1El.value === password2El.value) {
        passwordsMatch = true;
        password1El.style.borderColor = 'green';
    }   else {
        passwordsMatch = false;
        message.textContent = 'Make sure passwords match.';
        message.style.color = 'red';
        messageContainer.style.borderColor = 'red';
        password1El.style.borderColor = 'red';
        password1E2.style.borderColor = 'red';
    }
    //If form is valid and password match 
    if (isValid && passwordsMatch) {
        message.textContent = 'Succsessfully Registered!'
        message.style.color = 'green';
        messageContainer.style.borderColor = 'green';
    }
}

function storeFormData() {
    const user = {
        name: form.name.value,
        phone: form.phone.value,
        email: form.email.value,
        website: form.website.value,
        password: form.password.value
    };
    //Do someting with user data
    console.log(user);
}

//passes event once submit clicked
//preventing the form to refresh is the preventDefault function
function processFormData(e) {
    e.preventDefault();
    //Validate Form
    validateForm();
    //Submit Data if Valid
    if (isValid && passwordsMatch) {
        storeFormData();
    }
}

//Event Listner
//Once submit pushed, it calls procces form function 
form.addEventListener('submit', processFormData);