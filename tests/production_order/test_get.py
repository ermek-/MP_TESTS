from endpoints.production_order.get import GetOrder
from tests.payload_utils import get_payload_path, load_json

def test_get_production_order(auth_headers):
    endpoint = GetOrder()
    endpoint.get_object(headers=auth_headers)
    assert endpoint.check_response_code_is_(200)
    schema_path = get_payload_path("production_order", "get_orders_schema.json")
    schema = load_json(schema_path)
    endpoint.validate_json_schema(schema)
