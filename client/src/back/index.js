import 'formdata-polyfill';
import React from 'react';
import ReactDOM from 'react-dom';
import {Router} from 'react-router-dom';
import {History} from 'src/constants';
import App from './App';

ReactDOM.render(
    <Router history={History}>
        <App />
    </Router>,
    document.getElementById('app'),
);
