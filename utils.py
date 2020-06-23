import requests

import constants

class ProductSearchAPI():
    def __init__(self, api_endpoint, data):
        self.api_endpoint = api_endpoint
        self.data = data
        self.headers = constants.HEADERS

    def call_product_search_api(self):
        response = requests.post(self.api_endpoint, self.data, headers=self.headers)
        if response.ok:
            return response.text
        else:
            return '{} : {}'.format(response.status_code, response.reason)
