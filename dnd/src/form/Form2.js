import * as React from 'react';
import ReactDOM from "react-dom";
import { useForm } from 'react-hook-form';
import "./style2.css";

//creating a form with react hooks

function Form2() {
  //useForm hook has 3 arrays: register, handleSubmit, errors
  const { register, handleSubmit, errors } = useForm();
  const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
  const onSubmit = (data) => {
      console.log(data);
  };

  // const validateUserName = async (value) => {
  //   await sleep(1000);
  //   if (value === 'bill') return true;

  //   return false;
  // };
  

  return (
    <form className="App" onSubmit={handleSubmit(onSubmit)}>
      <h1>Sign Up</h1>
      <label>First Name:</label>
      <input name="firstName"  ref={ register({ required: true, minLength: 2 }) }
      />
      {errors.firstName && errors.firstName.type === "required" && (
      <p>This is required</p>
      )}

      {errors.firstName && errors.firstName.type === "minLength" && (
      <p>This field requires min length of 2 </p>
      )}

      <label>Last Name:</label>
      <input name="lastName" ref={ register({ required: true }) } />
      {errors.lastName && (<p>This is required</p>)}

      <label>Gender</label>
      <select name="gender" ref={ register({ required: true }) }>
        <option value="" >Select...</option>
        <option value="male">Male</option>
        <option value="female">Female</option>
      </select>

      <label>Username</label>
      <input name="username" ref={ register({ required: true }) } />

        {/* An input line To validate username */}
      {/* <input name="username" ref={ register({ required: true, validate: validateUserName }) } /> */}
      {errors.username && (<p>This is required</p>)}

      <label>Email</label>
      <input name="email" ref={ register({ required: true }) } />
      {errors.email && (<p>This is required</p>)}

      <label>About you</label>
      <textarea name="aboutYou" ref={ register({ required: true }) } />

      <input type="submit" />
    </form>
  );
}

export default Form2;


// const rootElement = document.getElementById("root");
// ReactDOM.render(<App />, rootElement);
