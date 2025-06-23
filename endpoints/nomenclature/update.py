import requests
from endpoints.base_endpoint import Endpoint

class UpdateNomenclature(Endpoint):
    def update_object(self, payload, headers, nomenclature_id):
        self.response = requests.put(
            f"{self.host}/Nomenclature/v1/nomenclatures/{nomenclature_id}/",
            json=payload,
            headers=headers,
        )
        self._log_request_response()
