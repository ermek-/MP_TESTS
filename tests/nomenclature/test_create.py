from endpoints.nomenclature.create import CreateNomenclature
from endpoints.nomenclature.delete import DeleteNomenclature
from tests.payload_utils import load_payload, get_payload_path

def test_create_nomenclature(auth_headers):
    endpoint = CreateNomenclature()
    payload_path = get_payload_path("nomenclature", "create_nomenclature.json")
    payload = load_payload(payload_path)
    endpoint.new_object(headers=auth_headers, payload=payload)
    nomenclature_id = endpoint.response_json["id"]
    assert endpoint.check_response_code_is_(201)
    assert endpoint.check_name(payload['name'])

    delete_endpoint = DeleteNomenclature()
    delete_endpoint.delete_object(nomenclature_id=nomenclature_id, headers=auth_headers)
    assert delete_endpoint.check_response_code_is_(200)
