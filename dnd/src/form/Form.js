import React from 'react';
import './style.css';

class Form extends React.Component {

    render() {
        return (
            <div className="container">
                <h1>Form Validation</h1>
                {/* form */}
                <div id="form">
                    <div className="form group">
                        <label for="name" >Full Name</label>
                        <input type="text" id="name" placeholder="Full Name"/>
                    </div>
                    {/* <!-- Phone Nuber --> */}
                    <div className="form group">
                        <label for="phone" >Phone</label>
                        <input type="tel" id="phone" placeholder="555-555-5555"/>
                    </div>
                    {/* <!-- email --> */}
                    <div className="form group">
                        <label for="email" >Email</label>
                        <input type="email" id="email" placeholder="email@adress.com"/>
                    </div>
                    {/* <!-- Website Url --> */}
                    <div className="form group">
                        <label for="Website" >Website URL</label>
                        <input type="url" id="Website" placeholder="http://Website.com"/>
                    </div>
                    {/* <!-- Password --> */}
                    <div className="form group">
                        <label for="password1" >Password</label>
                        <input type="password" id="password1" placeholder="Create password"/>
                    </div>
                    {/* <!-- Confirm Password --> */}
                    <div className="form group">
                        <label for="password2" >Confirm Password</label>
                        <input type="password" id="password2" placeholder="Confirm password"/>
                    </div>
                    <button type="submit">Register</button>
                </div>
                    <div className="message-container">
                        <h3 id="message">Don't Hesitate!</h3>
                    </div>
            </div>

        )
    }
}

export default Form;
