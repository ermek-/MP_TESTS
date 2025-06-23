from endpoints.nomenclature.get import GetNomenclature
from tests.payload_utils import get_payload_path, load_json

def test_get_nomenclature(auth_headers):
    endpoint = GetNomenclature()
    endpoint.get_object(headers=auth_headers)
    assert endpoint.check_response_code_is_(200)

    # schema_path = get_payload_path("production_order", "get_orders_schema.json")
    # schema = load_json(schema_path)
    # assert endpoint.validate_json_schema(schema)

def test_get_nomenclature_with_incorrect_schema(auth_headers):
    endpoint = GetNomenclature()
    endpoint.get_object(headers=auth_headers)
    assert endpoint.check_response_code_is_(200)

    # schema_path = get_payload_path("production_order", "get_order_schema.json")
    # schema = load_json(schema_path)
    # assert endpoint.validate_json_schema(schema)