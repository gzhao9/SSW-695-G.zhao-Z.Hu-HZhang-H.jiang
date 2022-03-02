class InputBoxComponent extends React.Component{
    
    render(){
        const {text, inputBoxType, parent} = this.props
        return (<div>
                    <div className="loginsPageText">{text}<br/></div>
                    <div><input type={inputBoxType} className="inputBox" onChange={this.props.updateProps}/></div>
                </div>
            )
    }

} 

export default InputBoxComponent