"""Endpoint helpers for creating production orders."""

import requests  # pylint: disable=import-error

from endpoints.base_endpoint import Endpoint


class CreateOrder(Endpoint):
    """API wrapper for creating production orders."""

    def new_object(self, payload: dict, headers: dict) -> None:
        """Send a request to create a new order."""

        self.response = requests.post(
            f"{self.host}/ProductionOrder/v1/ProductionOrders/",
            json=payload,
            headers=headers,
        )
        self.response_json = self.response.json()
        self._log_request_response()

    def check_number(self, number: str) -> None:
        """Check that the created order number equals the expected one."""

        assert self.response_json["number"] == number
