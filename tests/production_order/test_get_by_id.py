from endpoints.production_order.create import CreateOrder
from endpoints.production_order.get_by_id import GetByIdOrder
from tests.payload_utils import load_payload, get_payload_path, load_json

def test_get_by_id_production_order(auth_headers):
    create_endpoint = CreateOrder()
    payload_path = get_payload_path("production_order", "create_production_order.json")
    payload = load_payload(payload_path)
    create_endpoint.new_object(payload=payload, headers=auth_headers)
    order_id = create_endpoint.response_json["id"]

    endpoint = GetByIdOrder()
    endpoint.get_by_id_object(order_id=order_id, headers=auth_headers)
    endpoint.check_status_code(200)
    schema_path = get_payload_path("production_order", "get_order_schema.json")
    schema = load_json(schema_path)
    endpoint.validate_json_schema(schema)
