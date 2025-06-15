import requests
from endpoints.base_endpoint import Endpoint

class GetOrder(Endpoint):
    def new_object(self, headers):
        self.response =  requests.get(
            f'{self.host}/ProductionOrder/v1/ProductionOrders/',
            headers=headers
        )
        self.response_json = self.response.json()
        self._log_request_response()