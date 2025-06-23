import requests
from endpoints.base_endpoint import Endpoint

class GetNomenclatureFullInfo(Endpoint):
    def get_object(self, headers, nomenclature_id):
        self.response =  requests.get(
            f'{self.host}/Nomenclature/v1/nomenclatures/{nomenclature_id}/full-info/',
            headers=headers
        )
        self.response_json = self.response.json()
        self._log_request_response()