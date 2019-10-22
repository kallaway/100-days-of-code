import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <span className="Controls">
          <button><strong>B</strong></button>
          <button><em>I</em></button>
          <button><u>U</u></button>
        </span>
        <textarea rows="5" className="Text">hello</textarea>
      </header>
    </div>
  );
}

export default App;
