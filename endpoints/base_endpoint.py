class Endpoint:
    response = None
    response_json = None
    host = 'http://www.api.dev.pkmt.tech'

    def check_response_is_200(self):
        assert self.response.check_response_is_200() == 200