import requests

from endpoints.base_endpoint import Endpoint


class CreateOrder(Endpoint):
    def new_object(self, payload, headers):
        self.response = requests.post(
            f"{self.host}/ProductionOrder/v1/ProductionOrders/",
            json=payload,
            headers=headers,
        )
        self.response_json = self.response.json()
        self._log_request_response()

    def check_number(self, number):
        assert self.response_json["number"] == number

