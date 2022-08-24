const simpleColors = ["purple", "green", "crimson", "violet", "orange"];
const color = document.querySelector('.color');
const btn = document.getElementById('btn');

btn.addEventListener('click', () => {
    let idx = getRandom(simpleColors);
    color.textContent = simpleColors[idx];
    color.style.color = simpleColors[idx];
    document.body.style.backgroundColor = simpleColors[idx];
})

function getRandom(array) {
    return Math.floor(Math.random() * array.length);
}