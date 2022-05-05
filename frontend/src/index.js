import React from 'react'
import { createRoot, } from 'react-dom/client'
import { Provider } from 'react-redux'
import { Helmet } from 'react-helmet'

import App from './App'
import store from './redux/store'

import './index.scss'
import favicon from './favicon.png'

import $ from'jquery'
import Popper from'popper.js'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min'

import reportWebVitals from './reportWebVitals'

const container = document.getElementById('root')
const root = createRoot(container)

root.render(
  <React.StrictMode>
    <Helmet>
      <link 
        rel="icon" 
        type="image/png"
        href={favicon}
      />
    </Helmet>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>
)


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
