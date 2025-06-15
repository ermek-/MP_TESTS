"""Tests for retrieving orders by identifier."""

from endpoints.production_order.get_by_id import GetByIdOrder

def test_get_by_id_production_order(auth_headers) -> None:
    """Retrieve a specific order and check the response."""

    endpoint = GetByIdOrder()
    endpoint.get_by_id_object(order_id=27, headers=auth_headers)
    endpoint.check_status_code()
