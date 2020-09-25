import React from 'react';
import './style.css';

class Form extends React.Component {
    constructor(){
        super();
        this.state = {
            isValid: false,
            name: '',
            phone: '',
            email: '',
            password1: '',
            password2: '',
            message: ''
        }
    }

    textInput = (e) => {
        // console.log('value:', e.target.value);
        this.setState({[e.target.name]: e.target.value})
    }

    validateForm(e) {
        console.log(e.target.name);

    }

    processFormData() {
        validateForm();
    }

    render() {
        const { name } = this.state;
        return (
            <div className="container">
                <h1>Form Validation</h1>
                {/* form */}
                <div id="form">
                    <div className="form group">
                        <label htmlFor="name" >Full Name</label>
                        <input 
                        type="text" 
                        id="name" 
                        name="name" 
                        value={this.state.name} 
                        onChange={this.textInput} 
                        placeholder="Full Name"
                        required minLength="3" 
                        maxLength="100"/>
                    </div>
                    {/* <!-- Phone Nuber --> */}
                    <div className="form group">
                        <label htmlFor="phone" >Phone</label>
                        <input 
                        type="tel" 
                        id="phone" 
                        placeholder="555-555-5555"
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
                                required/>
                    </div>
                    {/* <!-- Password --> */}
                    <div className="form group">
                        <label htmlFor="password1" >Password</label>
                        <input type="password" id="password1" placeholder="Create password (Min. 8 charcters)"
                                required pattern="^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$"
                                title="Please include at least 1 Uppercase charcter, 1 lower case charcter, and 1 number."/>
                    </div>
                    {/* <!-- Confirm Password --> */}
                    <div className="form group">
                        <label htmlFor="password2" >Confirm Password</label>
                        <input type="password" id="password2" placeholder="Confirm password"
                                required pattern="^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$"/>
                    </div>
                    <button type="submit" 
                    onClick={() => processFormData()}
                    >Register</button>
                </div>
                    <div className="message-container">
                        <h3 id="message">Don't Hesitate!</h3>
                    </div>
            </div>

        )
    }
}

export default Form;
