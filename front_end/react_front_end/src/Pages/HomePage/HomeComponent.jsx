import React, { Component } from 'react'
import './HomePage.css'
import logo from './logo.svg';

export default class HomeComponent extends Component {
  render() {
    return (
        <div className="Home">
        <header className="Home-header">
          <img src={logo} className="Home-logo" alt="logo" />
          <p>
            Welcome to Calorie Shop!
          </p>
          <a
            className="Home-link"
            href="https://reactjs.org"
          >
            Sign in
          </a>
        </header>
      </div>
    )
  }
}
