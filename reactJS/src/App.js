import React, { Component } from "react"
import { setLocation } from "./actions/chat_action"
import Nav from "./components/Nav"
import SideBar from "./components/SideBar"
import Chat from "./components/Chat"
import "./App.css"

class App extends Component {

  render() {
    return (
      <div className="root">
        <Nav />
        <SideBar />
        <Chat />
      </div>
    );
  }
}

export default App