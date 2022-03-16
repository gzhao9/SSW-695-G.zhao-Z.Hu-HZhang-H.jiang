import React, { Component } from 'react'
import {Link, useRoutes} from 'react-router-dom'
import { Button } from 'antd';
import './HomePage.css'
import logo from './logo.png';

export default function HomeComponent() {
  return (
    <div className="Home">
        <header className="Home-header">
          <img src={logo} className="Home-logo" alt="logo" />
          <br />
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
          <br />
          <Link
            className="Home-link"
            to="/getUserInfoPage"
          >
            Input User Info
          </Link>
        </header>
      </div>
  )
}

