let myNodeList = document.getElementsByTagName("LI");
let i;

for(i = 0; i < myNodeList.length; i++) {
    let span = document.createElement ("SPAN");
    let txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    myNodeList[i].appendChild(span);
}

let close = document.getElementsByClassName("close");
let i1;

for (i1 = 0; i1 < close.length; i1++) {
    close[i1].onclick = function() {
        let div = this.parentElement;
        div.style.display = "none";
    }
}

let list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
    if(ev.target.tagName ==='LI') {
        ev.target.classList.toggle('checked');
    }
}, false);

function newElement() {
    let li = document.createElement("li");
    let inputValue = document.getElementById("myInput").value;
    let t = document.createTextNode(inputValue);
    li.appendChild(t);
    if (inputValue ==='') {
        alert("You must write someting!");
    } else {
        document.getElementById("liste").appendChild(li);
    }
document.getElementById("myInput").value = "";

let span2 = document.createElement("SPAN");
let txt2 = document.createTextNode("\u00D7");
span2.className = "close";
span2.appendChild(txt2);
li.appendChild(span2);

for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
        let div = this.parentElement;
        div.style.display = "none";
    }
}
}