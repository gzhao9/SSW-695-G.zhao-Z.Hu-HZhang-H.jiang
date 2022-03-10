import React, { Component } from 'react'
import {Link} from 'react-router-dom'
import './HomePage.css'
import logo from './logo.svg';

export default class HomeComponent extends Component {
  render() {
    return (
        <div className="Home">
        <header className="Home-header">
          <img src={logo} className="Home-logo" alt="logo" />
          <p className="Home-link">
            Welcome to Calorie Shop!
          </p>
          <br />
          <Link
            className="Home-link"
            to="/login"
          >
            Sign in
          </Link>
          <br />
          <Link
            className="Home-link"
            to="/foodPage"
          >
            Start Calorie Shopping!
          </Link>
        </header>
      </div>
    )
  }
}
