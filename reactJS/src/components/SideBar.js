import React from "react"
import { setLocation } from "../actions/chat_action"
import { connect } from "react-redux"
import { bindActionCreators } from "redux"


class SideBar extends React.Component {

    componentDidMount() {
        // fetch("https://ipinfo.io").then(res => res.json().then(data => { console.log(data) }))
        // navigator.geolocation.getCurrentPosition((position) => {
        //     console.log(position.coords.latitude.toFixed(2) + "," + position.coords.longitude.toFixed(2))
        //     fetch("https://maps.googleapis.com/maps/api/geocode/json?latlng=" +
        //         position.coords.latitude.toFixed(2) + "," + position.coords.longitude.toFixed(2) +
        //         "&key=AIzaSyB2T3V59a4UT2--vEUKw-KVI78lueAy9ds").then(res => res.json().then(data => {
        //             for (var i in data.results) {
        //                 for (var j in data.results[i].types)
        //                     if (data.results[i].types[j] === "administrative_area_level_1") {
        //                         this.props.setLocation(
        //                             position.coords.latitude.toFixed(2),
        //                             position.coords.longitude.toFixed(2),
        //                             data.results[i].formatted_address,
        //                         )
        //                     }
        //             }

        //             console.log("location", data)
        //         }))
        // })
    }

    render() {
        return (
            <div className="sidebar">
                <h4>{this.props.chat.city}</h4>
                <span>
                    <strong>
                        {this.props.chat.lat} / {this.props.chat.lon}
                    </strong>
                </span>
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
        setLocation,
    }, dispatch)
}

export default connect(mapeStateToProps, matchDispatchToProps)(SideBar)