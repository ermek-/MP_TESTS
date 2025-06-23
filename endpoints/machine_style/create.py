import requests
from endpoints.base_endpoint import Endpoint

class CreateMachineStyle(Endpoint):
    def new_object(self, payload, headers):
        self.response = requests.post(
            f"{self.host}/machine_styles/v1/",
            json=payload,
            headers=headers,
        )
        self.response_json = self.response.json()
        self._log_request_response()

    def check_name(self, name):
        return self.response_json["name"] == name
