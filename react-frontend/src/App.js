import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <a>
          Below token came from flask:
        </a>
          <p>{window.token}</p>
      </header>
    </div>
  );
}

export default App;
