"""Tests for retrieving production orders."""

from endpoints.production_order.get import GetOrder

def test_get_production_order(auth_headers) -> None:
    """Request the list of orders and check the status code."""

    endpoint = GetOrder()
    endpoint.get_object(headers=auth_headers)
    endpoint.check_status_code()
