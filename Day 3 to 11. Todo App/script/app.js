const mainContainer = document.querySelector('.main');
const themeToggle = document.querySelector('.theme-toggle');
const todoInputField = document.querySelector('.enterTodo');
const todoParentContainer = document.querySelector('.todo-list');
const todoGrandParentContainer = document.querySelector('.container-shadow');
const emptyTodo = document.querySelector('.empty-todo');
const todoFilter = document.querySelector('.todo-section-btns');
const itemCount = document.querySelector('.item-count');
let filterBtnArray = Array.from(document.querySelectorAll('.btn'));
const clearBtn = document.querySelector('.btn-clear');
let inputFieldArray;


// Switch dark and light mode
themeToggle.addEventListener('click', () => {
  mainContainer.classList.toggle('darkTheme-active');
})

// main functionality

let todoListItems = [];
let itemId = 0;
let itemState = 'active';
itemCount.textContent = todoListItems.length;

window.addEventListener('keydown', (e) => {
  if(e.key === 'Enter'){
    if(todoInputField.value !== '') {
      itemId++;
      let enteredTodoItem = todoInputField.value;

      let todoItemInfo = {
        id:itemId,
        itemValue: enteredTodoItem,
        state: itemState
      }

      todoListItems.push(todoItemInfo);
      updateTodoHTML(todoListItems);
      itemCount.textContent = todoListItems.length;
      todoInputField.value = '';     
    }
  }
});

checkboxFunction();
refreshTodoFilter();

function updateTodoHTML(todoListArray) {
  if(todoListArray.length > 0){
    let result = todoListArray.map((item) => {
      return `
        <div class="input-field todo-list-inputField" data-id=${item.id} data-state=${item.state}>
          <div class="checkbox-container" data-id=${item.id}>
            <img src="./images/icon-check.svg" alt="checkmark" class="checkmark" data-id=${item.id}>
          </div>
          <p class="text-field todoItem" data-id=${item.id}>${item.itemValue}</p>
          <img src="./images/icon-cross.svg" alt="cancel button" class="cancel-btn" data-id=${item.id}>
      </div>
    `
    }).join('');
    emptyTodo.style.display = 'none';
    todoParentContainer.style.display = 'block';
    todoParentContainer.innerHTML = result;  
    inputFieldArray = Array.from(document.querySelectorAll('.todo-list-inputField'));    
  } else {
    todoParentContainer.style.display = 'none';
    emptyTodo.style.display = 'grid';
  }
}

function checkboxFunction() {
  todoParentContainer.addEventListener('click', (e) => {
    let targetClass = e.target.classList;
     let parentContainer = e.target.parentElement;
     let grandParentContainer = e.target.parentElement.parentElement;
     let targetId = e.target.dataset.id;
     let parentId = parentContainer.dataset.id;
     let grandParentId = grandParentContainer.dataset.id;

    if(targetClass.contains('checkbox-container')){
      parentContainer.classList.toggle('active-checkbox');
      // console.log(targetId, parentId);
      if(targetId == parentId){
        let textValue = parentContainer.children[1];
        textValue.classList.toggle('completed-Todo');
        
        for(let i = 0; i < todoListItems.length; i++){
          let todoItemId = todoListItems[i].id;
          if(textValue.classList.contains('completed-Todo')){
            if(targetId == todoItemId){
              todoListItems[i].state = 'completed';
              inputFieldArray[i].dataset.state = 'completed';
              return;
            }
            
          } else {
            todoListItems[i].state = 'active';
            inputFieldArray[i].dataset.state = 'active';
            return
          }

        }
      }
    } 


    if (targetClass.contains('checkmark')) {
      grandParentContainer.classList.toggle('active-checkbox');
      if(targetId == grandParentId){
        // console.log(targetId, grandParentId);
        let textValue = grandParentContainer.children[1];
        textValue.classList.toggle('completed-Todo');
        for(let i = 0; i < todoListItems.length; i++){
          let todoItemId = todoListItems[i].id;
          if(!textValue.classList.contains('completed-Todo')){
            if(targetId == todoItemId){
              todoListItems[i].state = 'active';
              inputFieldArray[i].dataset.state = 'active';
              // updateTodoHTML(todoListItems);
              return;
            }
          } 
        }
      }
    }

    if(targetClass.contains('cancel-btn')){
      for(let i = 0; i < todoListItems.length; i++){
        if(targetId == parentId){
          parentContainer.classList.add('hide-input-field');
          todoListItems.splice(i, 1);
          // updateTodoHTML(todoListItems);
          itemCount.textContent = todoListItems.length;
          return;
        }
      }
    }
  })
}

function refreshTodoFilter() {
  todoFilter.addEventListener('click', (e) => {
    let filterBtnClass = e.target.classList;
    let filterState = e.target.dataset.filter;

    filterBtnArray.map((e) => {
      if(e.classList.contains('active-section')){
        e.classList.remove('active-section');
      }
    })
    filterBtnClass.add('active-section');

    if(filterBtnClass.contains('btn-complete')){
      for(let i = 0; i < inputFieldArray.length; i++){
        let inputFieldClasses = inputFieldArray[i].classList;
        let inputFieldState = inputFieldArray[i].dataset.state;
        // inputFieldClasses.remove('hide-input-field');
        if(inputFieldState !== 'completed'){
          inputFieldClasses.add('hide-input-field');
        } else {
          inputFieldClasses.remove('hide-input-field');
        }
      }
    }

    if(filterBtnClass.contains('btn-active')){
      for(let i = 0; i < inputFieldArray.length; i++){
        let inputFieldClasses = inputFieldArray[i].classList;
        let inputFieldState = inputFieldArray[i].dataset.state;
        inputFieldClasses.remove('hide-input-field');
        if(inputFieldState !== 'active'){
          inputFieldClasses.add('hide-input-field');
        } else {
          inputFieldClasses.remove('hide-input-field');
        }
      }
    }

    if(filterBtnClass.contains('btn-all')){
      for(let i = 0; i < inputFieldArray.length; i++){
        let inputFieldClasses = inputFieldArray[i].classList;
        inputFieldClasses.remove('hide-input-field');
      }
    }

  //   let todoSections = todoListItems.filter((item) => {
  //     if(filterState == item.state){
  //       return item;
  //     }
  //   });
  
  //   if(filterState == 'all'){
  //     updateTodoHTML(todoListItems);
  //   } else {
  //     updateTodoHTML(todoSections);
  //   }
  })
}







