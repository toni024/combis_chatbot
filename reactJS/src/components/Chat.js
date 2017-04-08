import React from "react"
import { connect } from "react-redux"
import { bindActionCreators } from "redux"
import { addMessage } from "../actions/chat_action"
import "../reset.css"
import "../style.css"

class Chat extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            msg_txt: "",
        }
    }

    componentDidMount() {
        this.setState({ msg_txt: "" })
        // document.getElementById("")
    }

    handleChange(e) {
        this.setState({ msg_txt: e.target.value })
    }

    handleKeyPress(e) {
        if (e.key === "Enter")
            this.props.addMessage(this.state.msg_txt)
    }

    render() {
        return (
            <div className="container">
                <div className="left">

                </div>
                <div className="right">
                    <div className="top">
                        <span><strong>CHATBOT</strong></span>
                    </div>
                    <div className="chaty">
                        {!this.props.chat.messages.length ? <h2>No messages...</h2> :
                            <div className="scroll">
                                {this.props.chat.messages.map((item, i) => (
                                    <div key={i} >
                                        {item.id === "user" ?
                                            <div className="bubble you">
                                                {item.message}
                                            </div> :
                                            <div className="bubble me">
                                                {item.message}
                                            </div>
                                        }
                                    </div>
                                ))}
                            </div>
                        }
                    </div>
                    <div className="write">
                        <input type="text" onKeyPress={this.handleKeyPress.bind(this)} onChange={this.handleChange.bind(this)} />
                        <a href="#" className="write-link send" onClick={() => this.props.addMessage(this.state.msg_txt, this.props.chat.lon, this.props.chat.lat)}></a>
                    </div>
                </div>
            </div>
        )
    }
}

function mapeStateToProps(state) {
    return {
        chat: state
    }
}

function matchDispatchToProps(dispatch) {
    return bindActionCreators({
        addMessage,
    }, dispatch)
}

export default connect(mapeStateToProps, matchDispatchToProps)(Chat)