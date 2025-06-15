import requests
from endpoints.base_endpoint import Endpoint

class DeleteOrder(Endpoint):
    def delete_object(self, headers, order_id):
        self.response =  requests.delete(
            f'{self.host}/ProductionOrder/v1/ProductionOrders/{order_id}/',
            headers=headers
        )
        self._log_request_response()

    def check_status_code(self):
        assert self.response == 200