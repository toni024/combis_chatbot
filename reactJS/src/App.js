import React, { Component } from "react"
import Nav from "./components/Nav"
import SideBar from "./components/SideBar"
import "./App.css"

class App extends Component {
  render() {
    return (
      <div className="root">
        <Nav />
        <SideBar />
      </div>
    );
  }
}

export default App