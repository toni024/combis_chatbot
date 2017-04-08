import React from "react"
import { connect } from "react-redux"
import { bindActionCreators } from "redux"
import { addMessage } from "../actions/chat_action"
import $ from "jquery"
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
    }

    handleChange(e) {
        this.setState({ msg_txt: e.target.value })
    }

    handleKeyPress(e) {
        $(".chaty").stop().animate({
            scrollTop: $(".chaty")[0].scrollHeight
        }, 100)
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
                            <div>
                                {this.props.chat.messages.map((item, i) => (
                                    <div key={i} >
                                        {item.id === "user" ?
                                            < div className="bubble me" >
                                                <div>
                                                    {console.log("aaaa", !(item.message.weather))}
                                                    {!item.message.google_maps ? "" :
                                                        < div >
                                                            {item.message.google_maps.link ? <img src={item.message.google_maps.link} alt="" /> : ""}
                                                            {item.message.google_maps.name ? <div>{item.message.google_maps.name}</div> : ""}
                                                            {item.message.google_maps.address ? <div>{item.message.google_maps.address}</div> : ""}
                                                        </div>}
                                                    {!(item.message.weather) ? "" :
                                                        <div>
                                                            {console.log("ssss", item.message.weather)}
                                                            {item.message.weather.length > 0 ? <div>{item.message.weather[0].temp} ℃</div> : "asd"}
                                                            {item.message.weather.length > 0 ? <div>{item.message.weather[0].desc}</div> : "asds"}
                                                        </div>}
                                                    {item.message.text ? <div>{item.message.text}</div> : ""}
                                                </div>
                                            </div> :
                                            <div className="bubble you">
                                                {item.message.text}
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