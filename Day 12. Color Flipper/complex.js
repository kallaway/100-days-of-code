const hexColors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"];
const color = document.querySelector('.color');
const btn = document.getElementById('btn');

btn.addEventListener('click', () => {
     let hexColor = '#';

     for(let i = 0; i < 6; i++){
          let idx = getRandom(hexColors);
          hexColor += hexColors[idx];
     }
     color.textContent = hexColor;
     color.style.color = hexColor;
    document.body.style.backgroundColor = hexColor;     
})

function getRandom(arr) {
     return Math.floor(Math.random() * arr.length);
 }