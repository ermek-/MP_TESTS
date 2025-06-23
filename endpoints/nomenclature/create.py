import requests
from endpoints.base_endpoint import Endpoint

class CreateNomenclature(Endpoint):
    def new_object(self, payload, headers):
        self.response = requests.post(
            f"{self.host}/Nomenclature/v1/nomenclatures/",
            json=payload,
            headers=headers,
        )
        self.response_json = self.response.json()
        self._log_request_response()

    def check_name(self, name):
        return self.response_json["name"] == name
