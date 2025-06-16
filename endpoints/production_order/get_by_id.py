import requests
from endpoints.base_endpoint import Endpoint

class GetByIdOrder(Endpoint):
    def get_by_id_object(self, headers, order_id):
        self.response =  requests.get(
            f'{self.host}/ProductionOrder/v1/ProductionOrders/{order_id}/',
            headers=headers
        )
        self.response_json = self.response.json()
        self._log_request_response()
