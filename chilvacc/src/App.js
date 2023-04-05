import React from 'react';
import Chatbot from 'react-chatbot-kit'
import 'react-chatbot-kit/build/main.css'
import './App.css'
import ActionProvider from './compenents/ActionProvider';
import MessageParser from './compenents/MessageParser';
import config from './config';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Chatbot config={config} actionProvider={ActionProvider} messageParser={MessageParser} />
      </header>
    </div>
  );
}

export default App;
