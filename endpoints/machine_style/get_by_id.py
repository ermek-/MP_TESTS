import requests
from endpoints.base_endpoint import Endpoint

class GetMachineStyleById(Endpoint):
    def get_object_by_id(self, headers, machine_style_id):
        self.response =  requests.get(
            f'{self.host}/machine_styles/v1/{machine_style_id}/',
            headers=headers
        )
        self.response_json = self.response.json()
        self._log_request_response()
