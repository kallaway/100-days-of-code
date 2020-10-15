import React from 'react';
import './style.css';

class Form4 extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            isValid: false,
            passwordsMatch: false,
            name: '',
            email: '',
            password: '',
            message: 'Dont Hesitate'
        }
    }

        //Get value from name input
        onNameChange = (e) => {
            this.setState({name: e.target.value})
        }

        //Get value from email input
        onEmailChange = (e) => {
            this.setState({email: e.target.value})
        }
    
        //Get value from password input
        onPasswordChange = (e) => {
            this.setState({password: e.target.value})
        }


        //Add all messages and Dom changes according to the data submitted
        // validateForm = (props) => {
        //     const form = 
        //     const { isValid } = this.state;
        //     console.log(isValid);
        //     if (isValid) {
        //         this.setState({message: 'Please fill out all fields'});
        //         //block return statement, that ends crawling the script
        //         return;
        //     }
        // }        

        processFormData(e) {
            // e.preventDefault();
            const form = e.target
            const ifValid = form.checkValidity()
            // Validate Form
            // validateForm(props);
            // Submit Data if Valid
            if (ifValid) {
                const user = {
                    name: this.state.name,
                    email: this.state.email,
                    password: this.state.password
                }
                console.log(user);
            }
            console.log('process', ifValid );
        }

        // storeFormData = () => {
        //     const user = {
        //         name: this.state.name,
        //         email: this.state.email,
        //         password: this.state.password
        //     }
        //     console.log(user);
        // }

    render() {
        // console.log('isValid:', this.state.isValid);
        const {message} = this.state;
        return (
            <div className="container">
                <h1>Form Validation</h1>
                {/* form */}
                <form onSubmit={this.handleSubmit}>
                    <div className="form group">
                        <label htmlFor="name" >Full Name</label>
                        <input 
                        type="text" 
                        id="name" 
                        name="name" 
                        value={this.state.name} 
                        onChange={this.onNameChange} 
                        placeholder="Full Name"
                        required minLength="3" 
                        maxLength="100"/>
                    </div>
                    {/* <!-- email --> */}
                    <div className="form group">
                        <label htmlFor="email" >Email</label>
                        <input 
                        type="email" 
                        id="email" 
                        value={this.state.email} 
                        onChange={this.onEmailChange} 
                        placeholder="email@adress.com"
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
                        <input type="password" id="password2" placeholder="Confirm password" onChange={this.onPasswordChange}
                                required pattern="^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$"/>
                    </div>
                    <button type="submit" 
                    value="Submit"
                    onClick={ this.processFormData() }
                    // disabled={(this.state.name === "" || this.state.name.length > 8 || this.state.email === "" || this.state.password === "") ? true : false }
                    >Register</button>
                </form>
                    <div className="message-container">
                        <h3 id="message">{ message } </h3>
                    </div>
                    <div className="flex flex-wrap mt-6">
                  <div className="w-1/2">
                    <a
                      href="#pablo"
                      onClick={e => e.preventDefault()}
                      className="text-gray-300"
                    >
                      <small>Forgot password?</small>
                    </a>
                  </div>
                  <div className="w-1/2 text-right">
                    <a
                      href="#pablo"
                      onClick={e => e.preventDefault()}
                      className="text-gray-300"
                    >
                      <small>Create new account</small>
                    </a>
                  </div>
                </div>
            </div>

        )
    }
}

export default Form4;
