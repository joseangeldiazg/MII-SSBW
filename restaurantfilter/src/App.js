import React, { Component } from 'react';
import logo from './logo.ico';
import './App.css';

const TIPOS = [
  { cuisine: "Tapas"},
  { cuisine: "Granaina"}
];

class RestaurantDisplay extends Component {
  constructor() {
    super();
    this.state = {
      restaurantesData: null
    };
  }
  componentDidMount() {
    const cuisine = this.props.cuisine;
    const URL = "http://localhost:8000/restaurantes/api/restaurants/?cuisine=" +cuisine;
    fetch(URL).then(res => res.json()).then(json => {
      this.setState({ restaurantesData: json });
    });
  }
  render() {
    const restaurantesData = this.state.restaurantesData;
    if (!restaurantesData) return <div>Loading</div>;
    return <div>{JSON.stringify(restaurantesData)}</div>;
  }
}


class App extends Component {
  constructor() {
    super();
    this.state = {
      activePlace: 0,
    };
  }
  render() {
    const activePlace = this.state.activePlace;
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Bienvenido a Restaurant Filter</h2>
        </div>
        <p className="App-intro">
          Esta app se conecta a la API desarrollada en <a href="https://github.com/joseangeldiazg/MII-SSBW/tree/master/django/sitio_web">este repositorio</a>
        </p>

        {TIPOS.map((place, index) => (
          <button
            key={index}
            onClick={() => {
            this.setState({ activePlace: index });
          }}>
            {place.cuisine}
          </button>
        ))}
        <RestaurantDisplay
         key={activePlace}
         cuisine={TIPOS[activePlace].cuisine}
       />
      </div>
    );
  }
}

export default App;
