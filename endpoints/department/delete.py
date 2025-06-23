import requests
from endpoints.base_endpoint import Endpoint

class DeleteDepartment(Endpoint):
    def delete_object(self, headers, department_id):
        self.response =  requests.delete(
            f'{self.host}/departments/v1/{department_id}/',
            headers=headers
        )
        self._log_request_response()
