//START

//SELECTORS
let taskInput = document.querySelector('#myInput');
let addTaskButton = document.querySelector('#button');
let taskList = document.querySelector('#list');


//EVENT LISTENERS

addTaskButton.addEventListener('click',addTask);



//FUNCTIONS

function addTask() {

    //PREVENT THE FORM FROM SUBMITING
    event.preventDefault();

    if(taskInput.value === "") {
        alert("Please enter a task!")
    }
    else {
         //CREATE TASK DIV
        let taskDiv = document.createElement('div');
        taskDiv.classList.add('task');

        //CREARE LI
        let taskLi = document.createElement('li');
        taskLi.innerText = taskInput.value;
        taskLi.classList.add('task-li');
        taskDiv.appendChild(taskLi);

        //CHECK BUTTON
        let checkButton = document.createElement('button');
        checkButton.innerHTML = '<i class="bx bx-check"></i>';
        checkButton.classList.add('check-btn');
        taskDiv.appendChild(checkButton);

        //DELETE BUTTON
        let deleteButton = document.createElement('button');
        deleteButton.innerHTML = '<i class="bx bx-eraser"></i>';
        deleteButton.classList.add('delete-btn');
        taskDiv.appendChild(deleteButton);

        taskList.appendChild(taskDiv);

        //CLEAR INPUT VALUE
        taskInput.value = '';


        deleteButton.addEventListener('click', () => {
            taskDiv.remove()
        });

    }
}