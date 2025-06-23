from endpoints.nomenclature.create import CreateNomenclature
from endpoints.nomenclature.get_by_id import GetByIdNomenclature
from tests.payload_utils import load_payload, get_payload_path, load_json

def test_get_by_id_nomenclature(auth_headers):
    create_endpoint = CreateNomenclature()
    payload_path = get_payload_path("nomenclature", "create_nomenclature.json")
    payload = load_payload(payload_path)
    create_endpoint.new_object(payload=payload, headers=auth_headers)
    nomenclature_id = create_endpoint.response_json["id"]
    assert create_endpoint.check_response_code_is_(201)

    endpoint = GetByIdNomenclature()
    endpoint.get_by_id_object(nomenclature_id=nomenclature_id, headers=auth_headers)
    assert endpoint.check_response_code_is_(200)

    # schema_path = get_payload_path("production_order", "get_order_schema.json")
    # schema = load_json(schema_path)
    # assert endpoint.validate_json_schema(schema)
