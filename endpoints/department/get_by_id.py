import requests
from endpoints.base_endpoint import Endpoint

class GetDepartmentById(Endpoint):
    def get_object_by_id(self, headers, department_id):
        self.response =  requests.get(
            f'{self.host}/departments/v1/{department_id}/',
            headers=headers
        )
        self.response_json = self.response.json()
        self._log_request_response()
