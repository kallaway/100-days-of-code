const mainContainer = document.querySelector('.main');
const themeToggle = document.querySelector('.theme-toggle');
const todoInputField = document.querySelector('.enterTodo');
const todoParentContainer = document.querySelector('.todo-list');
const todoGrandParentContainer = document.querySelector('.container-shadow');
const emptyTodo = document.querySelector('.empty-todo');
const todoSections = document.querySelector('.todo-section-btns');
const itemCount = document.querySelector('.item-count');
let filterBtnArray = Array.from(document.querySelectorAll('.btn'));
const clearBtn = document.querySelector('.btn-clear');
let inputFieldArray;

let todoListItems = [];
let itemId = 0;
let itemState = 'active';


// Switch dark and light mode
themeToggle.addEventListener('click', () => {
  mainContainer.classList.toggle('darkTheme-active');
})

window.addEventListener('keydown', (e) => {
  if(e.key === 'Enter'){
    if(todoInputField.value !== '') {
      
      updateTodoHtml();
      itemCount.textContent = todoParentContainer.childElementCount;
    }
  }
});

// window.addEventListener('DOMContentLoaded', displayItems);
// function displayItems(){
//   let items = getLocalStorage();
//   items.forEach((item) => {
//     createListItems(item.id, item.value);
//     todoListItems = Array.from(document.querySelectorAll('.todo-list-inputField'));
//   });

//   itemCount.textContent = todoParentContainer.childElementCount;
// }

function createListItems(id, value){
  
  const divElement = document.createElement('div');
  divElement.classList.add('input-field', 'todo-list-inputField')
  const idAttr = document.createAttribute('data-id');
  const stateAttr = document.createAttribute('data-state');
  idAttr.value = itemId;
  stateAttr.value = itemState;
  divElement.setAttributeNode(idAttr);
  divElement.setAttributeNode(stateAttr);
  
  divElement.innerHTML = `
    <div class="checkbox-container" data-id="${id}">
      <img src="./images/icon-check.svg" alt="checkmark" class="checkmark" data-id="${id}">
    </div>
    <p class="text-field todoItem" data-id="${id}">${value}</p>
    <img src="./images/icon-cross.svg" alt="delete button" class="delete-btn" data-id="${id}">
  `

  const deleteBtn = divElement.querySelector('.delete-btn');
  const checkboxes = divElement.querySelector('.checkbox-container');

  checkboxes.addEventListener('click', checkboxFunction)
  deleteBtn.addEventListener('click', deleteItem)

  todoParentContainer.appendChild(divElement);
  emptyTodo.style.display = 'none';
  todoParentContainer.style.display = 'block';
  setDefault();
}

function updateTodoHtml(){
  itemId++;
  let enteredTodoItem = todoInputField.value;

  createListItems(itemId, enteredTodoItem);
  todoListItems = Array.from(document.querySelectorAll('.todo-list-inputField'));
  addToLocalStorage(itemId, enteredTodoItem);
};

function deleteItem(e){
  let element = e.currentTarget.parentElement;
  const id = element.dataset.id;
  console.log(id);
  todoParentContainer.removeChild(element);
  let itemNumber = todoParentContainer.childElementCount;
  itemCount.textContent = itemNumber;
  
  if(itemNumber === 0){
    emptyTodo.style.display = 'grid';
    todoParentContainer.style.display = 'none';
  } 
  removeFromLocalStorage(id);
}

function setDefault(){
  todoInputField.value = '';
}

function checkboxFunction(e) {
  let targetClass = e.currentTarget.classList;
  let parentContainer = e.currentTarget.parentElement;
  let grandParentContainer = e.currentTarget.parentElement.parentElement;
  let targetId = e.currentTarget.dataset.id;
  let parentId = parentContainer.dataset.id;
  let grandParentId = grandParentContainer.dataset.id;

  
  if(targetClass.contains('checkbox-container')){
    parentContainer.classList.toggle('active-checkbox');
    // console.log(targetId, parentId);
    if(targetId == parentId){
      changeState(parentContainer);
    } 
  } 

  if (targetClass.contains('checkmark')) {
    grandParentContainer.classList.toggle('active-checkbox');
    if(targetId == grandParentId){
      changeState(grandParentContainer);
    }
  }
}

function changeState(container){
  let textValue = container.children[1];
  textValue.classList.toggle('completed-Todo');
  if(textValue.classList.contains('completed-Todo')){
    container.dataset.state = 'completed';
    // console.log(container);
  } else {
    container.dataset.state = 'active';
    // console.log(container);
  }
}


  todoSections.addEventListener('click', (e) => {
    let filterBtnClass = e.target.classList;
    let activeFilter = [];
    

    filterBtnArray.map((e) => {
      if(e.classList.contains('active-section')){
        e.classList.remove('active-section');
      }
    })

    filterBtnClass.add('active-section');

    todoListItems.map((e) => {
      if(e.classList.contains('hide-input-field')){
          e.classList.toggle('hide-input-field');
        }
  })

    if(filterBtnClass.contains('btn-active')){
      
      activeFilter = todoListItems.filter((item) => {
        if(!(item.dataset.state === 'active')){
          return item;
        }
      }); 
    }
    
    if(filterBtnClass.contains('btn-complete')){
      activeFilter = todoListItems.filter((item) => {
        if(!(item.dataset.state === 'completed')){
          return item;
        }
      }); 
    }

    activeFilter.forEach((item) => {
      item.classList.toggle('hide-input-field');
    })
  })

  clearBtn.addEventListener('click', () => {
    deleteItems();
  })

  function deleteItems(){
    let children = [...todoParentContainer.children];
    children.forEach(item => {
    if(item.dataset.state === "completed")
      todoParentContainer.removeChild(item);
    });
    itemCount.textContent = todoParentContainer.childElementCount;
  }

  function addToLocalStorage(id, value){
    let todo = {id, value}
    let items = getLocalStorage();
  
    items.push(todo);
    localStorage.setItem('list', JSON.stringify(items));
  }
  
  function getLocalStorage(){
    return localStorage.getItem('list')? JSON.parse(localStorage.getItem('list')): [];
  }
  
  function removeFromLocalStorage(id) {
    let items = getLocalStorage();
  
    items = items.filter((item) => {
      if(item.id != id){
        console.log(item);
        console.log(item.id, id);
        return item;
        
      }
    });

    localStorage.setItem('list', JSON.stringify(items));
  }

  

  
  
