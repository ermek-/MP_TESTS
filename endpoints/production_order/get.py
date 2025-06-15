"""Endpoints for retrieving production orders."""

import requests  # pylint: disable=import-error
from endpoints.base_endpoint import Endpoint

class GetOrder(Endpoint):
    """API wrapper for retrieving orders."""

    def get_object(self, headers: dict) -> None:
        """Request the list of production orders."""

        self.response = requests.get(
            f"{self.host}/ProductionOrder/v1/ProductionOrders/",
            headers=headers,
        )
        self.response_json = self.response.json()
        self._log_request_response()

    def check_status_code(self) -> None:
        """Ensure that the request completed successfully."""

        assert self.response.status_code == 200
