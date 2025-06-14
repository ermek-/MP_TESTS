from pathlib import Path

from endpoints.production_order.create import CreateOrder
from tests.payload_utils import load_payload

def test_create_production_order(auth_headers):
    endpoint = CreateOrder()
    payload_path = Path(__file__).resolve().parents[2] / "payloads" / "production_order" / "create_production_order.json"
    payload = load_payload(payload_path)
    endpoint.new_object(payload=payload, headers=auth_headers)
    endpoint.check_number(payload['number'])

