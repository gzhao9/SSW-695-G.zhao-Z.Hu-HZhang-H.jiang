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

    render(){
        return (
            <div>
                <LoginInputComponent text='username: ' inputBoxType='text' updateProps = {this.handleChangeUsername}/><br />
                <LoginInputComponent text='password: ' inputBoxType='password' updateProps = {this.handleChangePassword}/>
            </div>
        ) 
    }
}

ReactDOM.render(<LoginComponent/>, document.getElementById('login'))