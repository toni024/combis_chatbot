import React from "react"
import { connect } from "react-redux"
import { bindActionCreators } from "redux"
import { addMessage } from "../actions/chat_action"

class Chat extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            msg_txt: "",
        }
    }

    componentDidMount() {
        this.setState({ msg_txt: "" });
    }

    handleChange(e) {
        this.setState({ msg_txt: e.target.value });
    }

    render() {
        return (
            <div className="chat">
                {!this.props.chat.messages.length ? <h2>No messages....</h2> :
                    <div>
                        {this.props.chat.messages.map((item, i) => (
                            <div key={i} className="display_msg">
                                {/*{console.log(item.message)}*/}
                                {item.id === "user" ?
                                    <span className="user_msg">{item.message}</span> :
                                    <span className="bot_msg">{item.message}</span>
                                }
                            </div>
                        ))}
                    </div>}
                <div className="input">
                    <input type="text" onChange={this.handleChange.bind(this)} />
                    <button className="btn btn-primary" onClick={() => this.props.addMessage(this.state.msg_txt)}>send</button>
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