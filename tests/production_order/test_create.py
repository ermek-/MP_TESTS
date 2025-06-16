from endpoints.production_order.create import CreateOrder
from endpoints.production_order.delete import DeleteOrder
from tests.payload_utils import load_payload, get_payload_path

def test_create_production_order(auth_headers):
    endpoint = CreateOrder()
    payload_path = get_payload_path("production_order", "create_production_order.json")
    payload = load_payload(payload_path)
    endpoint.new_object(headers=auth_headers, payload=payload)
    order_id = endpoint.response_json["id"]
    assert endpoint.check_response_code_is_(201)
    assert endpoint.check_number(payload['number'])

    delete_endpoint = DeleteOrder()
    delete_endpoint.delete_object(order_id=order_id, headers=auth_headers)
    assert delete_endpoint.check_response_code_is_(200)
