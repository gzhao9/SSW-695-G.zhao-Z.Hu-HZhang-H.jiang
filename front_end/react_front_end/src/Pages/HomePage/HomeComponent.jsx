import React from "react";
import { Link } from "react-router-dom";
import "./HomePage.css";
import logo from "./logo.png";

export default function HomeComponent() {
  return (
    <div className="Home">
      <header className="Home-header">
        <img src={logo} className="Home-logo" alt="logo" />
        <br />
        <p className="Home-link">Welcome to Calorie Shop!</p>
        <br />
        <Link className="Home-link" to="/login">
          Sign in
        </Link>
        <Link className="Home-link" to="/userInfoPage">
          UserInfo (test link)
        </Link>
      </header>
    </div>
  );
}
