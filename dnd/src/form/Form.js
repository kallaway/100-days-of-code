import React from 'react';
import './style.css';

class Form extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            value: '',
            isValid: false,
            name: '',
            phone: '',
            email: '',
            url: '',
            password1: '',
            password2: '',
            message: 'Dont Hesitate'
        }
        this.handleChange = this.handleChange.bind(this);
        this.handlePhone = this.handlePhone.bind(this);
        this.handleEmail = this.handleEmail.bind(this);
        this.handleDomain = this.handleDomain.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    
      handleChange(event) {
        // this.setState({isValid: true})
        this.setState({name: event.target.value});
      }

      handlePhone(event) {
        this.setState({phone: event.target.value});
      }

      handleEmail(event) {
        this.setState({email: event.target.value});
      }

      handleDomain(event) {
        this.setState({url: event.target.value});
      }

    
      handleSubmit(event) {
        const valid = this.state.isValid
        if(valid === true) {
            alert('A name was submitted: ' + this.state.value);
            event.preventDefault();
        }
        else {
            // alert('Please fill in the fields')
            this.setState({message: 'Please fill out all fields'});
        }

      }

    render() {
        console.log('isValid:', this.state.isValid);
        const {message} = this.state
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
                        onChange={this.handleChange} 
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
                        value={this.state.phone} 
                        onChange={this.handlePhone} 
                        placeholder="555-555-5555"
                        required pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"/>
                    </div>
                    {/* <!-- email --> */}
                    <div className="form group">
                        <label htmlFor="email" >Email</label>
                        <input 
                        type="email" 
                        id="email" 
                        value={this.state.email} 
                        onChange={this.handleEmail} 
                        placeholder="email@adress.com"
                                required/>
                    </div>
                    {/* <!-- Website Url --> */}
                    <div className="form group">
                        <label htmlFor="Website" >Website URL</label>
                        <input type="url" id="Website" placeholder="http://Website.com"
                            value={this.state.url} 
                            onChange={this.handleDomain} 
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
                    value="Submit"
                    >Register</button>
                </form>
                    <div className="message-container">
                        <h3 id="message">{message}</h3>
                    </div>
            </div>

        )
    }
}

export default Form;
