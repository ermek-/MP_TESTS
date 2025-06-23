import requests
from endpoints.base_endpoint import Endpoint

class UpdateSubdivision(Endpoint):
    def update_object(self, payload, headers, subdivision_id):
        self.response = requests.put(
            f"{self.host}/departments/v1/{subdivision_id}/",
            json=payload,
            headers=headers,
        )
        self._log_request_response()
