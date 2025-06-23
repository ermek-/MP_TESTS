import requests
from endpoints.base_endpoint import Endpoint

class UpdateMachineStyle(Endpoint):
    def update_object(self, payload, headers, machine_style_id):
        self.response = requests.put(
            f"{self.host}/machine_styles/v1/{machine_style_id}/",
            json=payload,
            headers=headers,
        )
        self._log_request_response()
