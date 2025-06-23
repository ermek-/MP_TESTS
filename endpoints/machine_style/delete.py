import requests
from endpoints.base_endpoint import Endpoint

class DeleteMachineStyle(Endpoint):
    def delete_object(self, headers, machine_style_id):
        self.response =  requests.delete(
            f'{self.host}/machine_styles/v1/{machine_style_id}/',
            headers=headers
        )
        self._log_request_response()
