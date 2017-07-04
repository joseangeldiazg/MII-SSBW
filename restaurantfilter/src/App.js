import React, { Component } from 'react';
import logo from './logo.ico';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Bienvenido a Restaurant Filter</h2>
        </div>
        <p className="App-intro">
          Esta app se conecta a la API desarrollada en <a href="https://github.com/joseangeldiazg/MII-SSBW/tree/master/django/sitio_web">este repositorio</a>
        </p>
      </div>
    );
  }
}

export default App;
