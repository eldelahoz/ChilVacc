import React from "react";
import Chatbot from "react-chatbot-kit";
import "react-chatbot-kit/build/main.css";
import "./App.css";
import ActionProvider from "./compenents/ActionProvider";
import MessageParser from "./compenents/MessageParser";
import config from "./config";
import logo from "./image/ChilVaccSinFondo.png";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div>
          <h1>Bienvenidos a ChilVacc</h1>
          <div className="grid">
            <div className="imageLogo">
              <img src={logo} alt="logo" />
            </div>
            <div>
              <p>
                ChilVacc es una aplicación web con un chatbot para ayudar a los
                papás estar atentos con el esquema de vacunación de sus hijos y
                dar respuesta a esquema tardío de vacunación.
              </p>
            </div>
          </div>
        </div>
        <Chatbot
          config={config}
          actionProvider={ActionProvider}
          messageParser={MessageParser}
        />
      </header>
    </div>
  );
}

export default App;
