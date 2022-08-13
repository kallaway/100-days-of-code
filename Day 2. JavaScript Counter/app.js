// Assign Default Count Value
let count = 0;

// Target value & buttons 
const value = document.querySelector("#value");
const btns = document.querySelectorAll(".btn");

btns.forEach(function(btn) {
     btn.addEventListener('click', function(e) {
          const styles = e.currentTarget.classList;
          styles.contains("decrease") ? count-- : styles.contains("increase") ? count++ : count = 0;

          count > 0 ? value.style.color = "green" : count < 0 ? value.style.color = "red" : value.style.color = "#222";

          value.textContent = count;
     });
});


