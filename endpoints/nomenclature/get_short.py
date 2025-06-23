import requests
from endpoints.base_endpoint import Endpoint

class GetNomenclatureShortInfo(Endpoint):
    def get_object(self, headers, params):
        self.response =  requests.get(
            f'{self.host}/Nomenclature/v1/nomenclatures/short-info/',
            params=params,
            headers=headers
        )
        self.response_json = self.response.json()
        self._log_request_response()

    def check_prod_process_id(self, prod_process_id):
            return self.response_json["prod_process[0]"] == prod_process_id

    def all_prod_process_match(self, expected_prod_process: int) -> bool:
        try:
            response_json = self.response.json()
            if not isinstance(response_json, list):
                return False

            return all(item.get("prod_process") == expected_prod_process for item in response_json)
        except Exception:
            return False
