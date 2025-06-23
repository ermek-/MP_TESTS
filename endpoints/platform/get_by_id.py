import requests
from endpoints.base_endpoint import Endpoint

class GetPlatformById(Endpoint):
    def get_object_by_id(self, headers, platform_id):
        self.response =  requests.get(
            f'{self.host}/platforms/v1/{platform_id}/',
            headers=headers
        )
        self.response_json = self.response.json()
        self._log_request_response()
