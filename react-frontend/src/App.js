import React from 'react';
import garfield from "./garfield.png"
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
          <img src={garfield} alt="have some fun"/>
        <p>
          This token came from flask
        </p>
          <p>{window.token}</p>
      </header>
    </div>
  );
}

export default App;
