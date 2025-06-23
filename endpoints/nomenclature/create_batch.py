import requests
from endpoints.base_endpoint import Endpoint

class CreateBatchNomenclature(Endpoint):
    def new_object(self, payload, headers, nomenclature_id):
        self.response = requests.post(
            f"{self.host}/Nomenclature/v1/nomenclatures/{nomenclature_id}/create-batch/",
            json=payload,
            headers=headers,
        )
        self.response_json = self.response.json()
        self._log_request_response()

    def check_count(self, count):
        return self.response_json["count"] == count