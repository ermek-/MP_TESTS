from endpoints.production_order.create import CreateOrder
from tests.payload_utils import load_payload, get_payload_path


def test_create_production_order(auth_headers):
    endpoint = CreateOrder()
    payload_path = get_payload_path("production_order", "create_production_order.json")
    payload = load_payload(payload_path)
    endpoint.new_object(headers=auth_headers, payload=payload)
    endpoint.check_number(payload['number'])


