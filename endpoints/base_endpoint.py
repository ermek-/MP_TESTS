class Endpoint:
    response = None
    response_json = None
    host = 'http://www.api.dev.pkmt.tech'

    def check_response_is_200(self):
        """Verify that the last response returned HTTP 200."""
        assert self.response.status_code == 200
