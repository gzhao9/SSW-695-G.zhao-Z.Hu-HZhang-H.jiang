import logo from './logo.svg';
import './App.css';
import {BrowserRouter, Route, Routes, Link} from 'react-router-dom'
import LoginComponent from './Pages/LoginPage/LoginCompoment';
import HomeComponent from './Pages/HomePage/HomeComponent';
import SignUpComponent from './Pages/SignUpPage/SignUpComponent'
import FoodPage from './Pages/FoodInfoPage/FoodPage'

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomeComponent/>}/>
          <Route path="/login" element={<LoginComponent/>}/>
          <Route path="/signUp" element={<SignUpComponent/>}/>
          <Route path="/foodPage" element={<FoodPage/>}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
