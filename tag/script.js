var mainMap = document.getElementById('mapDiv'); //element I want to resize

//Resizing the element to be responsive
window.addEventListener('resize', checkBreakPoint);

function checkBreakPoint() {
        //width of viewport
        var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
        var h = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
        mainMap.children[0].setAttribute('width', w);
        mainMap.children[0].setAttribute('height', h);
}




