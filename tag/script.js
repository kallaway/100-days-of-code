var mainMap = document.getElementById('map'); //element I want to resize

//Resizing the element to be responsive
window.addEventListener("resize", checkBreakPoint);

function checkBreakPoint() {
        //width of viewport
        var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
        var h = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
        // console.log(mainMap.children[0]);
        // mainMap.children[0].style.width = w;
        mainMap.children[0].setAttribute('width', w);
        mainMap.children[0].setAttribute('height', h);
}

// The location should be a variable that can be changed 
// (before implementation) and the measurements should inherit the targeted element.



