import React from "react"
import Header from '../../Components/Header/Header'
import {Link,Route,useNavigate} from 'react-router-dom'
import SignUpComponent from "../SignUpPage/SignUpComponent"
import './LoginPage.css'
import '../../Components/ButtonWide/ButtonWide.css'
import '../../Components/InputBox/InputBox.css'


class LoginComponent extends React.Component{
    state = {username:'', password:''}
    
    handleChangeUsername = (event) => {
        this.setState({username:event.target.value})
    }
    handleChangePassword = (event) => {
        this.setState({password:event.target.value})
    }
    handleSubmit = (event) => {
        const{username, password} = this.state
        if(username == ''){
            alert('Please input the username')
            return
        }
        if(password == ''){
            alert('Please input the password')
            return
        }
        alert('Send request:\nusername: ' + username + '\npassword: ' + password)
    }

    render(){
        return (
            <div className="loginPg">
                <Header headerText='Sign in'/>
                <div style={{marginTop: '100px', marginBottom: '100px'}}>
                    <p className="loginText">Start your diet meal plan with Calorie Shopping!</p>
                </div>
                
                <div style={{marginBottom: '100px'}}>
                    <input type="text"  onChange={this.handleChangeUsername} className='inputBox' placeholder='Email' /><br />
                    <input type="password"  onChange={this.handleChangePassword} className='inputBox' placeholder='Password' /><br />
                </div>
                <div>
                    <button type="submit" onClick={this.handleSubmit} className="btnWide">Sign In</button><br/>
                    <p className="loginText">Or</p>
                    <Link to='/signUp'>Sign Up with Email</Link>
                </div>
            </div>
        ) 
    }
}

export default LoginComponent