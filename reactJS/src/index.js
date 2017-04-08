import React from "react"
import ReactDOM from "react-dom"
import { applyMiddleware, createStore } from "redux"
import { Provider } from "react-redux"
import logger from "redux-logger"
import thunk from "redux-thunk"

import chatReducer from "./reducers/chat_reducer"
import App from "./App"

const middleware = applyMiddleware(thunk, logger)

const store = createStore(chatReducer, middleware)

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById("root")
)
