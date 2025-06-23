import requests
from endpoints.base_endpoint import Endpoint

class DeleteSubdivision(Endpoint):
    def delete_object(self, headers, subdivision_id):
        self.response =  requests.delete(
            f'{self.host}/departments/v1/{subdivision_id}/',
            headers=headers
        )
        self._log_request_response()
