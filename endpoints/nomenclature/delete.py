import requests
from endpoints.base_endpoint import Endpoint

class DeleteNomenclature(Endpoint):
    def delete_object(self, headers, nomenclature_id):
        self.response =  requests.delete(
            f'{self.host}/Nomenclature/v1/nomenclatures/{nomenclature_id}/',
            headers=headers
        )
        self._log_request_response()
