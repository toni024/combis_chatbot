import React from "react"
import { connect } from "react-redux"
import { bindActionCreators } from "redux"
import { addMessage, setLocation } from "../actions/chat_action"
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
        $.getJSON('https://ipinfo.io', (data) => {
            var loc = data.loc.split(",")
            this.props.setLocation(loc[0].slice(0, 4), loc[1].slice(0, 4), data.city)
        })

    }

    handleChange(e) {
        this.setState({ msg_txt: e.target.value })
    }

    handleKeyPress(e) {
        if (e.key === "Enter")
            this.submitHandle()
    }

    componentDidUpdate(prevProps, prevState) {
        $(".chaty").stop().animate({
            scrollTop: $(".chaty")[0].scrollHeight
        }, 100)
    }


    submitHandle() {
        $(".chaty").stop().animate({
            scrollTop: $(".chaty")[0].scrollHeight
        }, 100)

        this.setState({ msg_txt: "" })
        this.props.addMessage(this.state.msg_txt, this.props.chat.lon, this.props.chat.lat)
    }

    render() {
        return (
            <div className="containera">
                <div className="left hidden-xs">
                    <div className="cont_wrap">
                        <img src="http://paybefore.com/wp-content/uploads/2016/11/Robot_icon.png" alt="" />
                        <h2>
                            I'm' Bruno!
                        </h2>
                    </div>
                </div>
                <div className="right">
                    <div className="top">
                        <span><strong>ChatBot</strong></span>
                    </div>
                    <div className="chaty">
                        {!this.props.chat.messages.length ? <h2>No messages...</h2> :
                            <div>
                                {this.props.chat.messages.map((item, i) => (
                                    <div key={i} >
                                        {!(item.id === "user") ?
                                            < div  > {/*bot*/}
                                                {item.message.google_maps ? <div>
                                                    {typeof item.message.google_maps !== "object" ? "" :
                                                        < div >
                                                            {item.message.google_maps.length > 0 ? <div>
                                                                {item.message.google_maps.map((place, i) => (
                                                                    <div key={i} className="bubble me">
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
                                                        {typeof item.message.weather !== "object" ? "" :
                                                            <div >
                                                                {item.message.weather.length > 0 ? <div>
                                                                    {item.message.weather.map((day, i) => (
                                                                        <div className="bubble me" key={i}>
                                                                            {(this.state.date.getDate() + i) > 9 ?
                                                                                (this.state.date.getDate() + i) : "0" + (this.state.date.getDate() + i)}.
                                                                                {this.state.date.getMonth() + 1 > 9 ? this.state.date.getMonth() : "0" + this.state.date.getMonth()}
                                                                            <i className={day.i}></i>
                                                                            {day.temp}℃ {day.description}
                                                                        </div>
                                                                    ))}
                                                                </div> : ""}
                                                            </div>}
                                                    </div> : ""}
                                                    {item.message.text ? <div >
                                                        {item.message.text !== "null" ? <div className="bubble me">{item.message.text}</div> : " "}
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
                        <input type="text" required placeholder="Enter message.." onKeyPress={this.handleKeyPress.bind(this)} onChange={this.handleChange.bind(this)} value={this.state.msg_txt} />
                        <a href="#" className="write-link send" onClick={this.submitHandle.bind(this)}></a>
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
        setLocation,
    }, dispatch)
}

export default connect(mapeStateToProps, matchDispatchToProps)(Chat)