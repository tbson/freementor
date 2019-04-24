import Enzyme from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import React from 'react';
import {shallow, mount, render} from 'enzyme';
import Tools from 'src/utils/helpers/Tools';
import {Service} from '../main_table/Row';

Enzyme.configure({adapter: new Adapter()});

beforeEach(() => {
    jest.restoreAllMocks();
});

describe('Service.removeRequest', () => {
    const id = 1;
    it('Normal case', () => {
        const apiCall = jest.spyOn(Tools, 'apiCall').mockImplementation(() => {});
        Service.removeRequest(id);
        expect(apiCall).toHaveBeenCalled();
        expect(apiCall.mock.calls[0][0]).toEqual(`http://localhost/api/v1/variable/${id}`);
        expect(apiCall.mock.calls[0][1]).toEqual({});
        expect(apiCall.mock.calls[0][2]).toEqual('DELETE');
    });
});

describe('Service.handleRemove', () => {
    const okResp = {
        ok: true,
        data: {
            key: 'value'
        }
    };
    const failResp = {
        ok: false,
        data: {
            key: 'value'
        }
    };
    const id = 1;
    it('On success', async () => {
        const removeRequest = jest.spyOn(Service, 'removeRequest').mockImplementation(async () => okResp);
        jest.spyOn(Tools, 'popMessageOrRedirect');

        const result = await Service.handleRemove(id);

        expect(Tools.popMessageOrRedirect).not.toHaveBeenCalled();
        expect(removeRequest).toHaveBeenCalled();
        expect(removeRequest.mock.calls[0][0]).toEqual(id);
        expect(result).toEqual({id});
    });

    it('On error', async () => {
        const removeRequest = jest.spyOn(Service, 'removeRequest').mockImplementation(async () => failResp);
        jest.spyOn(Tools, 'popMessageOrRedirect');

        const result = await Service.handleRemove(id);

        expect(Tools.popMessageOrRedirect).toHaveBeenCalled();
        expect(Tools.popMessageOrRedirect.mock.calls[0][0]).toEqual(failResp);
    });

    it('On exception', async () => {
        const removeRequest = jest.spyOn(Service, 'removeRequest').mockImplementation(async () => Promise.reject(failResp));
        jest.spyOn(Tools, 'popMessageOrRedirect');

        const result = await Service.handleRemove(id);

        expect(Tools.popMessageOrRedirect).toHaveBeenCalled();
        expect(Tools.popMessageOrRedirect.mock.calls[0][0]).toEqual(failResp);
    });
});
