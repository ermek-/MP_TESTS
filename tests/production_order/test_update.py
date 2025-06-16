from endpoints.production_order.create import CreateOrder
from endpoints.production_order.update import UpdateOrder
from endpoints.production_order.delete import DeleteOrder
from tests.payload_utils import load_payload, get_payload_path

def test_update_production_order(auth_headers):
    create_endpoint = CreateOrder()
    payload_path = get_payload_path("production_order", "create_production_order.json")
    payload = load_payload(payload_path)
    create_endpoint.new_object(payload=payload, headers=auth_headers)
    order_id = create_endpoint.response_json["id"]
    assert create_endpoint.check_response_code_is_(201)

    update_endpoint = UpdateOrder()
    payload_path = get_payload_path("production_order", "create_production_order.json")
    payload = load_payload(payload_path)
    update_endpoint.update_object(payload=payload, headers=auth_headers, order_id=order_id)
    assert update_endpoint.check_response_code_is_(200)

    delete_endpoint = DeleteOrder()
    delete_endpoint.delete_object(order_id=order_id, headers=auth_headers)
    assert delete_endpoint.check_response_code_is_(200)
