from endpoints.production_order.create import CreateOrder
from endpoints.production_order.delete import DeleteOrder
from endpoints.production_order.get_by_id import GetByIdOrder
from tests.payload_utils import load_payload, get_payload_path

def test_delete_production_order(auth_headers):
    create_endpoint = CreateOrder()
    payload_path = get_payload_path("production_order", "create_production_order.json")
    payload = load_payload(payload_path)
    create_endpoint.new_object(payload=payload, headers=auth_headers)
    order_id = create_endpoint.response_json["id"]

    delete_endpoint = DeleteOrder()
    delete_endpoint.delete_object(order_id=order_id, headers=auth_headers)

    get_by_id_endpoint = GetByIdOrder()
    get_by_id_endpoint.get_by_id_object(order_id=order_id, headers=auth_headers)
    assert get_by_id_endpoint.response.status_code == 404
