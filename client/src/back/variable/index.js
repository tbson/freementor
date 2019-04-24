// @flow
import * as React from 'react';
import {useEffect} from 'react';

export class Service {
    static method1() {
        return 1;
    }
}

export default () => {
    useEffect(() => {
        document.title = 'Variable manager';
    }, []);

    return <h1>Variable page</h1>;
};
