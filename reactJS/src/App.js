import React, { Component } from "react"
import Chat from "./components/Chat"

class App extends Component {

    render() {
        return (
            <div className="wrapper">
                <Chat />
            </div>
        );
    }
}

export default App