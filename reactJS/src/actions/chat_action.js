export const addMessage = (message, lon, lat) => {
    return (dispatch) => {
        fetch("/check", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message, lon, lat })
        }).then(res => {
            if (res.status === 200) {
                res.json().then(data => {
                    console.log("od bosaka", data)
                    dispatch({
                        type: "ADD_MESSAGE",
                        payload: { message: data, id: "bot" },
                    })
                })
            }
        })
        var data = { text: message }
        dispatch({
            type: "ADD_MESSAGE",
            payload: { message: data, id: "user" },
        })
    }
}

export const setLocation = (lon, lat, city) => {
    console.log()
    return {
        type: "SET_LOCATION",
        payload: { lon, lat, city }
    }
}