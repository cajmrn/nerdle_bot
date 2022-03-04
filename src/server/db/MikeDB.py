"""
Example Python interface with the Mike-DB no-SQL database
"""

import json

import requests


class MikeDB:

    # def __init__(self, db_host=DB_CONFIG.DB_HOST, db_name=DB_CONFIG.DB_NAME, db_key=DB_CONFIG.DB_KEY):
    def __init__(self, db_host, db_name, db_key):
        if not db_name:
            raise Exception('DB NAME can not be empty!')
        api_host = ('http://' + db_host) if db_host else ''
        self.dbUrl = api_host + '/mike-db/api/' + db_name + '/'
        ws_host = ('ws://' + db_host) if db_host else ''
        self.wsUrl = ws_host + '/mike-db/subscribe' + '/' + db_name
        self.dbKey = db_key

    def prepare_header(self, value, is_form_data=False):
        headers = {
            'API_KEY': self.dbKey  # always send api key with every request header
        }
        if value is str:
            headers['Content-Type'] = 'text/plain;charset=utf-8'
        elif is_form_data:
            headers['Content-Type'] = 'multipart/form-data'
        else:
            headers['Content-Type'] = 'application/json;charset=utf-8'

        return headers

    @staticmethod
    def prepare_value(value):
        return json.dumps(value) if value else None

    @staticmethod
    def validate_response(response):
        if response and (response.status_code == 200 or response.status_code == 201):
            # resource exists or was created
            if response.headers.get('content-type') == 'application/json':
                return response.json()
            else:
                return response.content

        elif response and response.status_code == 204:
            return None  # resource is empty

        elif response and (response.status_code or response.reason):
            message = 'Http error:'
            if response.status_code:
                message += '(' + response.status_code + ')'
            if response.reason:
                message += ' ' + response.reason
            raise Exception(message)

        elif response and response.text:
            raise Exception('Error: ' + response.text)  # server error

        elif response:
            raise Exception(response)  # unknown error
        else:
            raise Exception('No response')  # everything is bad

    """
    Retrieve an Object, Primitive or a Collection associated with the given Key
    @param key
    @param firstResult (optional) index of the first element in resulting collection to retrieve
    @param maxResults (optional) number of elements from resulting collection to retrieve
    @param fields  (optional) string of comma separated list of field names to populate in response
    @returns {*} 200 if record retrieved or status code 204 when no such record
    """
    def get(self, key, first_result=0, max_results=-1, fields=None):
        payload = {
            'firstResult': first_result,
            'maxResults': max_results
        }
        if fields:
            payload['fields'] = fields

        response = requests.get(self.dbUrl + key, headers=self.prepare_header(None), params=payload)
        return self.validate_response(response)

    """
    Add a single item to a collection associated with the Key.
    """
    def add(self, key, value, index=None):
        payload = {}
        if index:
            payload['index'] = index

        response = requests.post(self.dbUrl + key, data=self.prepare_value(value), headers=self.prepare_header(value),
                                 params=payload)
        return self.validate_response(response)

    """
    Modify a single item in a collection associated with the Key (if 'index' or values's 'id' is set).
    Or set a new (replace if exists) value associated with the Key. 
    """
    def update(self, key, value, index=None):
        payload = {}
        if index:
            payload['index'] = index

        response = requests.patch(self.dbUrl + key, data=self.prepare_value(value), headers=self.prepare_header(value),
                                  params=payload)
        return self.validate_response(response)

    """
    Delete a single item in a collection associated with the Key (if 'index' or values's 'id' is set).
    Or delete existing Key entirely.
    """
    def delete(self, key, value, index=None, id=None):
        payload = {}
        if index:
            payload['index'] = index
        if id:
            payload['id'] = id
        elif value and value.id:
            payload['id'] = value.id

        response = requests.delete(self.dbUrl + key, data=self.prepare_value(value), headers=self.prepare_header(value),
                                   params=payload)
        return self.validate_response(response)

    """
    Uploads a binary file and assosiates it with a Key.
    Requires properly constructed HTTP Form-Data value object.
    """
    def upload_file(self, key, form_data):
        if form_data and not form_data['file']:
            raise Exception("'file' must be set in FormData")

        # TODO: reportProgress: true,
        # TODO: observe: 'events'
        response = requests.post(self.dbUrl + key, data=form_data, headers=self.prepare_header(form_data, True))
        return self.validate_response(response)
