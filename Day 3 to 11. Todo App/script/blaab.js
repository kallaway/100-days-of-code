todoFilter.addEventListener('click', (e) => {
  let filterBtnClass = e.target.classList;
  if(filterBtnClass.contains('btn-complete')){
    const completedItems = todoListItems.filter((item) => {
      // console.log(item.status);
      return completedItems
    })
    console.log(completedItems);
  }
})

if(textValue.classList.contains('completed-Todo')){
          for(let i = 0; i < todoListItems.length; i++){
            let todoItemId = todoListItems[i].id;
            if(targetId = todoItemId){
              todoListItems[i].state = 'completed';
              return;
            }
          }
        }


        const mainContainer = document.querySelector('.main');
        const themeToggle = document.querySelector('.theme-toggle');
        // const todoListContainer = document.querySelector('.todo-list');
        let todoInputField = document.querySelector('.enterTodo');
        let todoParentContainer = document.querySelector('.todo-list');
        let todoGrandParentContainer = document.querySelector('.container-shadow');
        let emptyTodo = document.querySelector('.empty-todo');
        let todoFilter = document.querySelector('.info-panel');
        // let itemState = document.querySelector('.todo-list-inputField').dataset.state;
        // console.log(itemState);
        
        
        // Switch dark and light mode
        themeToggle.addEventListener('click', () => {
          mainContainer.classList.toggle('darkTheme-active');
        })
        
        // main functionality
        
        let todoListItems = [];
        let itemId = 0;
        let itemState = 'active';
        
        window.addEventListener('keydown', (e) => {
          if(e.key === 'Enter'){
            if(todoInputField.value !== '') {
              let enteredTodoItem = todoInputField.value;
        
        
              let todoItemInfo = {
                id:itemId,
                itemValue: enteredTodoItem,
                state: itemState
              }
              todoListItems.push(todoItemInfo);
              itemId++;
        
              if(todoListItems.length > 0) {
                updateTodoHTML();
                todoInputField.value = '';
                console.log(todoListItems);
              } 
            }
          }
        })
        
        checkboxFunction();
        
        function updateTodoHTML() {
          if(todoListItems.length > 0){
            let result = todoListItems.map((item) => {
              return `
                <div class="input-field todo-list-inputField" data-id=${item.id} data-state=${item.state}>
                  <div class="checkbox-container" data-id=${item.id}>
                    <img src="./images/icon-check.svg" alt="checkmark" class="checkmark">
                  </div>
                  <p class="text-field todoItem" data-id=${item.id}>${item.itemValue}</p>
                  <img src="./images/icon-cross.svg" alt="cancel button" class="cancel-btn" data-id=${item.id}>
              </div>
            `
            })
            emptyTodo.style.display = 'none';
            todoParentContainer.style.display = 'block';
            todoParentContainer.innerHTML = result.join('');
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
            //  console.log({targetClass}, {parentContainer}, {grandParentContainer},
            //   {targetId}, {parentId}, {grandParentId});
            console.log({targetId}, {parentId});
            if(targetClass.contains('checkbox-container')){
              parentContainer.classList.toggle('active-checkbox');
              if(targetId = parentId){
                // console.dir(parentContainer);
                let textValue = parentContainer.children[targetId];
                textValue.classList.toggle('completed-Todo'); 
        
                if(textValue.classList.contains('completed-Todo')){
                  for(let i = 0; i < todoListItems.length; i++){
                    let todoItemId = todoListItems[i].id;
                    if(targetId = todoItemId){
                      let selected = (todoListItems[todoItemId]);
                      console.log({selected});
                      console.log({targetId}, {todoItemId});
                      return;
                    }
                  }
                } 
              }
            } 
            else if (targetClass.contains('checkmark')) {
              grandParentContainer.classList.toggle('active-checkbox');
              if(targetId = grandParentId){
                let textValue = grandParentContainer.children[1];
                textValue.classList.toggle('completed-Todo');
        
                // if(!textValue.classList.contains('completed-Todo')){
                //   for(let i = 0; i < todoListItems.length; i++){
                //     todoListItems[i].state = 'active';
                //     console.log(todoListItems);
                //     return;
                //   }
                // }
              }
            }
        
            if(targetClass.contains('cancel-btn')){
              // console.log(targetId, parentId);
              for(let i = 0; i < todoListItems.length; i++){
                if(targetId = parentId){
                  todoListItems.splice(i, 1);
                  console.log(todoListItems);
                  updateTodoHTML();
                  return;
                }
              }
            }
          })
        }
        
        // todoFilter.addEventListener('click', (e) => {
        //   let filterBtnClass = e.target.classList;
        //   if(filterBtnClass.contains('btn-complete')){
        //     const completedItems = todoListItems.filter((item) => {
        //       // console.log(item.status);
        //       return completedItems
        //     })
        //     console.log(completedItems);
        //   }
        // })


        clearBtn.addEventListener('click', () => {
          for(let i = 0; i < inputFieldArray.length; i++){
            let inputFieldClasses = inputFieldArray[i].classList;
            let inputFieldState = inputFieldArray[i].dataset.state;
            if(inputFieldState == 'completed'){
              inputFieldClasses.add('hide-input-field');
              // updateTodoHTML(todoListItems);
            }
          }
          
        })
        
        
        
        