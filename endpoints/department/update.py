import requests
from endpoints.base_endpoint import Endpoint

class UpdateDepartment(Endpoint):
    def update_object(self, payload, headers, department_id):
        self.response = requests.put(
            f"{self.host}/departments/v1/{department_id}/",
            json=payload,
            headers=headers,
        )
        self._log_request_response()
