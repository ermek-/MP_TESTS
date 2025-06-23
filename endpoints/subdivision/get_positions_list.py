import requests
from endpoints.base_endpoint import Endpoint

class GetSubdivisionPositionsList(Endpoint):
    def get_object(self, headers, subdivision_id):
        self.response =  requests.get(
            f'{self.host}/subdivisions/{subdivision_id}/get_subdivision_positions_list/',
            headers=headers
        )
        self.response_json = self.response.json()
        self._log_request_response()