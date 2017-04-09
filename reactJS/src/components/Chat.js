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
            date: new Date(),
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
            this.props.addMessage(this.state.msg_txt, this.props.chat.lon, this.props.chat.lat)
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
                                        {!(item.id === "user") ?
                                            < div  > {/*bot*/}
                                                {item.message.google_maps ? <div>
                                                    {typeof item.message.google_maps != "object" ? "" :
                                                        < div >
                                                            {item.message.google_maps.length > 0 ? <div>
                                                                {item.message.google_maps.map((place, i) => (
                                                                    <div className="bubble me">
                                                                        <img src={place.link} alt="" />
                                                                        <h3>{place.name}</h3>
                                                                        {place.address}
                                                                        <br />
                                                                    </div>
                                                                ))}
                                                            </div> : ""}
                                                        </div>}
                                                </div> : ""}
                                                <div>
                                                    {item.message.weather ? <div>
                                                        {typeof item.message.weather != "object" ? "" :
                                                            <div >
                                                                {item.message.weather.length > 0 ? <div>
                                                                    {item.message.weather.map((day, i) => (
                                                                        <div className="bubble me">
                                                                            {(this.state.date.getDate() + i) > 9 ?
                                                                                (this.state.date.getDate() + i) : "0" + (this.state.date.getDate() + i)}.
                                                                                {this.state.date.getMonth() > 9 ? this.state.date.getMonth() : "0" + this.state.date.getMonth()}
                                                                            <i className={day.i}></i>
                                                                            {day.temp}℃ {day.description}
                                                                        </div>
                                                                    ))}
                                                                </div> : ""}
                                                            </div>}
                                                    </div> : ""}
                                                    {item.message.text ? <div >
                                                        {item.message.text != "null" ? <div className="bubble me">{item.message.text}</div> : " "}
                                                    </div> : ""}
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