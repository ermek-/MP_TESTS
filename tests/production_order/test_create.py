from endpoints.production_order.create import CreateOrder
from tests.payload_utils import load_payload
from pathlib import Path


def test_create_production_order(auth_headers):
    endpoint = CreateOrder()
    payload_path = Path(__file__).resolve().parents[2] / "data" / "production_order" / "create_production_order.json"
    payload = load_payload(payload_path)
    endpoint.new_object(headers=auth_headers, payload=payload)
    endpoint.check_number(payload['number'])


