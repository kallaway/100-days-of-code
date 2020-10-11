let count = 0;
let word = 0;
// find the div with id "value"
const value = document.querySelector('#value');

// select all buttons
const btns = document.querySelectorAll('.btn');

// loop through buttons, add event listener to each; increase or decrease count based on button clicked
btns.forEach(function (btn) {
    btn.addEventListener('click', function (e) {
        const styles = e.currentTarget.classList;
        if (styles.contains('decrease')) {
            
            count--;
        } else if (styles.contains('increase')) {
            
            count ++;
        } else count = 0;
        if (count > 0) {
            value.style.color = 'green';
        }
        if (count < 0) {
            value.style.color = 'red';
        }
        if (count === 0) {
            value.style.color = 'black';
        }

        if(count % 3 === 0 && count % 5 === 0) {
            word.textContent="Fizz";
            
        }

        if (count === 0) {
            document.getElementById("word").innerHTML="";
         } else if (count % 5 === 0 && count % 3 === 0) {
            document.getElementById("word").innerHTML="FizzBuzz";
            
            
        } else if (count % 3 === 0) {
            document.getElementById("word").innerHTML="Fizz";
            
        } else if (count % 5 === 0) {
            document.getElementById("word").innerHTML="Buzz";
            
        } else {
            document.getElementById("word").innerHTML="";
            
        }
        
        value.textContent = count;
         
    })
});