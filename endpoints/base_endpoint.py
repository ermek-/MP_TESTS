"""Base classes and utilities for API endpoints."""

import logging
from typing import Optional

import requests  # pylint: disable=import-error


logger = logging.getLogger(__name__)


class Endpoint:  # pylint: disable=too-few-public-methods
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

    def check_response_is_200(self) -> None:
        """Assert that the last response had a ``200`` status code."""

        assert self.response is not None
        assert self.response.status_code == 200
