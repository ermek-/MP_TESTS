import requests
from endpoints.base_endpoint import Endpoint

class UpdateOrder(Endpoint):
    def update_object(self, payload, headers, order_id):
        self.response = requests.put(
            f"{self.host}/ProductionOrder/v1/ProductionOrders/{order_id}/",
            json=payload,
            headers=headers,
        )
        self._log_request_response()
