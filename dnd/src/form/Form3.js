import * as React from 'react';
import ReactDOM from "react-dom";
import { useForm } from 'react-hook-form';
import './style.css';

function Form3() {

    const { register, handleSubmit, errors } = useForm();
    const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
    const onSubmit = (data) => {
        console.log(data);
    };

    return (
            <div className="container" >
                <h1>Form Validation</h1>
                {/* form */}
                <form onSubmit={handleSubmit(onSubmit)}>
                    <div className="form group">
                        <label>Name</label>
                        <input 
                        name="firstName" 
                        ref={ register({ required: true, minLength: 3 }) }
                        />
                        {errors.firstName && errors.firstName.type === "required" && (
                        <p>This is required</p>
                        )}

                        {errors.firstName && errors.firstName.type === "minLength" && (
                        <p>This field requires min length of 3 </p>
                        )}
                    </div>
                    {/* <!-- Phone Nuber --> */}
                    <div className="form group">
                        <label htmlFor="phone" >Phone</label>
                        <input 
                        type="tel" 
                        id="phone"
                        placeholder="555-555-5555"
                        ref={ register({ required: true, minLength: 12 }) }
                        required pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"/>
                    </div>
                    {/* <!-- email --> */}
                    <div className="form group">
                        <label htmlFor="email" >Email</label>
                        <input 
                        type="email" 
                        id="email" 
                        placeholder="email@adress.com"
                                required/>
                    </div>
                    {/* <!-- Website Url --> */}
                    <div className="form group">
                        <label htmlFor="Website" >Website URL</label>
                        <input type="url" id="Website" placeholder="http://Website.com"
                        />
                    </div>
                    {/* <!-- Password --> */}
                    <div className="form group">
                        <label htmlFor="password1" >Password</label>
                        <input type="password" id="password1" placeholder="Create password (Min. 8 charcters)"
                                />
                    </div>
                    {/* <!-- Confirm Password --> */}
                    <div className="form group">
                        <label htmlFor="password2" >Confirm Password</label>
                        <input type="password" id="password2" placeholder="Confirm password"
                            />
                    </div>
                    <button type="submit" 
                    value="Submit"
                    >Register</button>
                </form>
                    <div className="message-container">
                        <h3 id="message"></h3>
                    </div>
            </div>

    )
}

export default Form3;
