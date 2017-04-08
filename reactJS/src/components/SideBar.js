import React from "react"

class SideBar extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            lat: null,
            lon: null,
        }
    }

    componentDidMount() {
        navigator.geolocation.getCurrentPosition((position) => {
            this.setState({
                lat: position.coords.latitude.toFixed(2),
                lon: position.coords.longitude.toFixed(2),
            });
        })
    }

    render() {
        return (
            <div className="sidebar">
                <span>
                    {this.state.lat} / {this.state.lon}
                </span>
            </div>
        )
    }
}

export default SideBar