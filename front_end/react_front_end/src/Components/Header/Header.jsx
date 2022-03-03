import React, { Component } from 'react'
import './Header.css'

export default class Header extends Component {
  render() {
    const {headerText} = this.props
    return (<div className='headBackground'>
        <div className='headerText'>
            {headerText}
        </div>
    </div>
    )
  }
}
