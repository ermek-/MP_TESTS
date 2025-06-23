from endpoints.nomenclature.create import CreateNomenclature
from endpoints.nomenclature.delete import DeleteNomenclature
from endpoints.nomenclature.edit import EditNomenclature
from tests.payload_utils import load_payload, get_payload_path

def test_update_nomenclature(auth_headers):
    create_endpoint = CreateNomenclature()
    payload_path = get_payload_path("nomenclature", "create_nomenclature.json")
    payload = load_payload(payload_path)
    create_endpoint.new_object(payload=payload, headers=auth_headers)
    nomenclature_id = create_endpoint.response_json["id"]
    assert create_endpoint.check_response_code_is_(201)

    edit_endpoint = EditNomenclature()
    payload_path = get_payload_path("nomenclature", "create_nomenclature.json")
    payload = load_payload(payload_path)
    edit_endpoint.edit_object(payload=payload, headers=auth_headers, nomenclature_id=nomenclature_id)
    # assert edit_endpoint.check_response_code_is_(200)

    delete_endpoint = DeleteNomenclature()
    delete_endpoint.delete_object(nomenclature_id=nomenclature_id, headers=auth_headers)
    # assert delete_endpoint.check_response_code_is_(200)
