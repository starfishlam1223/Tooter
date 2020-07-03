import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
// import App from './App';
import { TootsComponent, TootDetailComponent } from './toots';
import * as serviceWorker from './serviceWorker';

const e = React.createElement

const tootElem = document.getElementById('tooter')

if (tootElem) {
  ReactDOM.render(e(TootsComponent, tootElem.dataset), tootElem);
}

const tootDetailElem = document.querySelectorAll(".tooter-detail")

tootDetailElem.forEach((container) => {
  if (container) {
    var path = window.location.pathname
    var idRegex = /(?<tootId>\d+)/
    var matches = path.match(idRegex)

    if (matches) {
      var tootId = matches.groups.tootId
      container.setAttribute("data-toot-id", tootId)  
      ReactDOM.render(e(TootDetailComponent, container.dataset), container);  
    }
  }
})

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
