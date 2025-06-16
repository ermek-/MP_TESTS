import logging
from typing import Optional

from jsonschema import validate

import requests

logger = logging.getLogger(__name__)

class Endpoint:
    """Base class for API endpoints."""

    response: Optional[requests.Response] = None
    response_json = None
    host = "http://www.api.dev.pkmt.tech"

    def _log_request_response(self) -> None:
        """Log request and response details for debugging."""

        if not self.response:
            return

        req = self.response.request
        logger.debug("Request %s %s", req.method, req.url)
        logger.debug("Request headers: %s", dict(req.headers))
        logger.debug("Request body: %s", req.body)

        logger.debug("Response status: %s", self.response.status_code)
        logger.debug("Response headers: %s", dict(self.response.headers))
        logger.debug("Response body: %s", self.response.text)

    def check_response_code_is_(self, status):
        return self.response.status_code == status

    def validate_json_schema(self, schema: dict) -> None:
        """Validate response JSON against the provided schema."""
        assert self.response_json is not None
        validate(self.response_json, schema)
