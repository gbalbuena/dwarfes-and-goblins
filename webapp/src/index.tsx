import React from "react";
import ReactDOM from "react-dom";




import reportWebVitals from './reportWebVitals';

import { BrowserRouter, Routes, Route } from "react-router-dom";

import './fonts/PressStart2P-Regular.ttf';
import "./index.css";
import App from "./App";
import { Home, Lore, About, Leaderboard, Wallet } from './Pages';

ReactDOM.render(
  <React.StrictMode>
      <BrowserRouter>
        <Routes>
          {/* <Route path="/" element={<App />}> */}
          <Route element={<App />}>
            <Route path="" element={<Home />} />
            <Route path="lore" element={<Lore />} />
            <Route path="leaderboard" element={<Leaderboard />} />
            <Route path="wallet" element={<Wallet />} />
            <Route path="about" element={<About />} />
          </Route>
        </Routes>
      </BrowserRouter>
  </React.StrictMode>,
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
