import React from 'react';
import SideBar from './sidebar';
import ResultsParser from './results_parser.js'

import './App.css';

export default function App() {
  return (
    <div id="App">
      <SideBar />
      <div id="header">
        <h1>Whale of a good time. A look at Virtual Machine Performance</h1>
      </div>
      <div id="Body">
      
      </div>
      <div id="footer">
      <p> Written by Tish Konz, Andrew Hill and John Becker </p>
      </div>
    </div>
  );
}

