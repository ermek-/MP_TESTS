import requests
from endpoints.base_endpoint import Endpoint

class UpdatePlatform(Endpoint):
    def update_object(self, payload, headers, platform_id):
        self.response = requests.put(
            f"{self.host}/platforms/v1/{platform_id}/",
            json=payload,
            headers=headers,
        )
        self._log_request_response()
