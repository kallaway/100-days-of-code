

function handleClick(e) {
    console.log("handleClick -> e)", e.target.dataset);
    var total = 0;
    if (e.target.dataset.action === 'calculate') {
        // const result = view.value.match(/[+\-]*(\.\d+|\d+(\.\d+)?)/g) || [];
        // while(result.length){
        //     total+= parseFloat(result.shift());
        // }
        // I know that eval i snot good practice but it's the simpliest way to check the result
        view.value = eval(view.value);
    }
    else if (e.target.dataset.action === 'clear')
        view.value = '';
    else view.value += e.target.dataset.num ? e.target.dataset.num : e.target.dataset.action;
}

const buttons = document.querySelectorAll("button");
const view = document.querySelector('input[type="text"]');

buttons.forEach(btn => btn.addEventListener('click', handleClick));
