const initialState = {
    messages: [{ id: "user", message: "nesta" }, { id: "bot", message: "nesta drugo" }],
    lon: null,
    lat: null,
    city: null,
}

export default (state = initialState, action) => {
    switch (action.type) {
        case "ADD_MESSAGE":
            return {
                ...state,
                messages: [...state.messages, action.payload],
            }
        case "SET_LOCATION":
            return {
                ...state,
                lon: action.payload.lon,
                lat: action.payload.lat,
                city: action.payload.city,
            }
        default: return state
    }
}