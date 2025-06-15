import requests
from endpoints.base_endpoint import Endpoint

class GetOrder(Endpoint):
    def get_object(self, headers):
        self.response =  requests.get(
            f'{self.host}/ProductionOrder/v1/ProductionOrders/',
            headers=headers
        )
        self.response_json = self.response.json()
        self._log_request_response()

    def check_status_code(self):
        assert self.response is not None
        assert self.response.status_code == 200
