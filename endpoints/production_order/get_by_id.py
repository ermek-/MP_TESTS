"""Endpoint helpers for retrieving a production order by ID."""

import requests  # pylint: disable=import-error
from endpoints.base_endpoint import Endpoint

class GetByIdOrder(Endpoint):
    """API wrapper for retrieving an order by its ID."""

    def get_by_id_object(self, headers: dict, order_id: int) -> None:
        """Retrieve a single production order by identifier."""

        self.response = requests.get(
            f"{self.host}/ProductionOrder/v1/ProductionOrders/{order_id}/",
            headers=headers,
        )
        self.response_json = self.response.json()
        self._log_request_response()

    def check_status_code(self) -> None:
        """Ensure that the request for the order ID was successful."""

        assert self.response.status_code == 200
