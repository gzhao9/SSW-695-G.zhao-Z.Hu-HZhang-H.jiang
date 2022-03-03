import React, { Component } from 'react'
import Header from '../../Components/Header/Header'
import '../../Components/ButtonWide/ButtonWide.css'
import './SignUpPage.css'

export default class SignUpComponent extends Component {
  state = {username: '', password: '', confirmPassword: ''}
  handleChangeUsername = (event) => {
      this.setState({username:event.target.value})
  }
  handleChangePassword = (event) => {
      this.setState({password:event.target.value})
  }
  handleChangeConfirmPassword = (event) => {
      this.setState({confirmPassword:event.target.value})
  }
  handleSubmit = (event) => {
    const {username, password, confirmPassword} = this.state
    if(username === ''){
      alert('Please input the username')
      return
    }
    if(password === ''){
      alert('Please input the password')
      return
    }
    if(!this.checkEmail(username)){
      alert('Invalid Email address!')
      return
    }
    if(!this.checkPassword(password)){
      alert('Invalid Password!')
      return
    }
    if(confirmPassword !== password){
      alert('Please input the same password')
      return
    }
    alert('Send request:\nusername: ' + username + '\npassword: ' + password)
  }

  checkEmail(email){
    const words = email.split('@')
    if(words.length !== 2){
      return false
    }
    const tail = words[1].split('.')
    if(tail.length !== 2){
      return false
    }
    return true
  }

  checkPassword(password){
    return password.length <= 32 && password.length >= 8
  }


  render() {
    return (
      <div className="signupPg">
        <Header headerText='Sign up'/>
        <div style={{marginTop: '100px', marginBottom: '100px'}}>
            <p className="signupText">Start your diet meal plan with Calorie Shopping!</p>
        </div>
        
        <div style={{marginBottom: '100px'}}>
            <input type="text"  onChange={this.handleChangeUsername} className='inputBox' placeholder='Email' /><br />
            <input type="password"  onChange={this.handleChangePassword} className='inputBox' placeholder='Password (8 ~ 32 characters)' /><br />
            <input type="password"  onChange={this.handleChangeConfirmPassword} className='inputBox' placeholder='Confirm Password' /><br />
        </div>
        <div>
            <button type="submit" onClick={this.handleSubmit} className="btnWide">Start the Calorie Shopping!</button><br/>
        </div>
        
      </div>
    )
  }
}
