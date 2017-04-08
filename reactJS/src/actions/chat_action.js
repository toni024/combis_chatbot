export const addMessage = (message) => {
    return (dispatch) => {
        fetch("/check", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        }).then(res => {
            if (res.status === 200) {
                res.json().then(data => {
                    console.log("od bosaka", data)
                    dispatch({
                        type: "ADD_MESSAGE",
                        payload: { message, id: "user" },
                    })
                    dispatch({
                        type: "ADD_MESSAGE",
                        payload: { message: data.text, id: "bot" },
                    })
                })
            }
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