class LoginInputComponent extends React.Component{
    render(){
        const {text, inputBoxType, parent} = this.props
        return (<div>
                    <div className="loginPageText">{text}<br/></div>
                    <div><input type={inputBoxType} className="inputBox" onChange={this.props.updateProps}/></div>
                </div>
            )
    }
} 

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
    handleBack = (event) => {
        window.history.back(-1)
    }

    render(){
        return (
            <div>
                <LoginInputComponent text='username: ' inputBoxType='text' updateProps = {this.handleChangeUsername}/><br />
                <LoginInputComponent text='password: ' inputBoxType='password' updateProps = {this.handleChangePassword}/><br/>
                <button type="submit" onClick={this.handleSubmit} className="loginBtn">Login</button>
                <button onClick={this.handleBack} className="loginBtn">Back</button>
            </div>
        ) 
    }
}

ReactDOM.render(<LoginComponent/>, document.getElementById('login'))