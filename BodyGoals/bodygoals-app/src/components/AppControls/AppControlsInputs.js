import React from 'react'

const  AppControlsInputs = () => {
    return (
        <div className= "app__controls">
        <div className= "app__controls__inputs">
         <input type="text"
         placeholder="Meal"
         value=""
         />

         <input type="number"
         placeholder="Calories"
         />

         <button>Add Meal</button>




        </div>
        </div>
    )
}

export default AppControlsInputs
