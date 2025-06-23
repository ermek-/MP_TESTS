import requests
from endpoints.base_endpoint import Endpoint

class GetDepartmentsChief(Endpoint):
    def get_object(self, headers):
        self.response =  requests.get(
            f'{self.host}/departments/v1/get_chief/',
            headers=headers
        )
        self.response_json = self.response.json()
        self._log_request_response()