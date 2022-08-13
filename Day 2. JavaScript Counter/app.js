// Assign Default Class
let count = 0;

// Target value & buttons 
const value = document.querySelector("#value");
const btns = document.querySelectorAll(".btn");

// method 1
/* btns.forEach(function(btn) {
     btn.addEventListener('click', function(e) {
          const styles = e.currentTarget.classList;
          if (styles.contains("decrease")) {
               count--;
          } else if (styles.contains("increase")) {
               count++;
          }else {
               count = 0;
          }
          value.textContent = count;
     });
}); */

// method 2
btns.forEach(function(btn) {
     btn.addEventListener('click', function(e) {
          const styles = e.currentTarget.classList;
          styles.contains("decrease") ? count-- : styles.contains("increase") ? count++ : count = 0;

          count > 0 ? value.style.color = "green" : count < 0 ? value.style.color = "red" : value.style.color = "#222";

          value.textContent = count;
     });
});


