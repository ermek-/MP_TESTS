import requests
from endpoints.base_endpoint import Endpoint

class GetNomenclature(Endpoint):
    def get_object(self, headers):
        self.response =  requests.get(
            f'{self.host}/Nomenclature/v1/nomenclatures/',
            headers=headers
        )
        self.response_json = self.response.json()
        self._log_request_response()