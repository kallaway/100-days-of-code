var element = document.getElementById('element');
var resizer = document.createElement('div');
resizer.className = 'resizer';
resizer.style.width = '10px';
resizer.style.height = '10px';
resizer.style.background = 'red';
resizer.style.position = 'absolute';
resizer.style.right = 0;
resizer.style.bottom = 0;
resizer.style.cursor = 'se-resize';
element.appendChild(resizer);
resizer.addEventListener('mousedown', initResize, false);

function initResize(e) {
   window.addEventListener('mousemove', Resize, false);
   window.addEventListener('mouseup', stopResize, false);
}
function Resize(e) {
   element.style.width = (e.clientX - element.offsetLeft) + 'px';
   element.style.height = (e.clientY - element.offsetTop) + 'px';
} 
function stopResize(e) {
    window.removeEventListener('mousemove', Resize, false);
    window.removeEventListener('mouseup', stopResize, false);
}