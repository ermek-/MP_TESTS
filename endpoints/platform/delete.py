import requests
from endpoints.base_endpoint import Endpoint

class DeletePlatform(Endpoint):
    def delete_object(self, headers, platform_id):
        self.response =  requests.delete(
            f'{self.host}/platforms/v1/{platform_id}/',
            headers=headers
        )
        self._log_request_response()
