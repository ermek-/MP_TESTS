from endpoints.production_order.create import CreateOrder
from endpoints.production_order.update import UpdateOrder
from endpoints.production_order.delete import DeleteOrder
from tests.payload_utils import load_payload
from pathlib import Path

def test_update_production_order(auth_headers):
    create_endpoint = CreateOrder()
    payload_path = Path(__file__).resolve().parents[2] / "data" / "production_order" / "create_production_order.json"
    payload = load_payload(payload_path)
    create_endpoint.new_object(payload=payload, headers=auth_headers)
    order_id = create_endpoint.response_json["id"]

    update_endpoint = UpdateOrder()
    payload_path = Path(__file__).resolve().parents[2] / "data" / "production_order" / "create_production_order.json"
    payload = load_payload(payload_path)
    update_endpoint.update_object(payload=payload, headers=auth_headers, order_id=order_id)

    delete_endpoint = DeleteOrder()
    delete_endpoint.delete_object(order_id=order_id, headers=auth_headers)
