from endpoints.nomenclature.create import CreateNomenclature
from endpoints.nomenclature.delete import DeleteNomenclature
from endpoints.nomenclature.get_by_id import GetByIdNomenclature
from tests.payload_utils import load_payload, get_payload_path

def test_delete_nomenclature(auth_headers):
    create_endpoint = CreateNomenclature()
    payload_path = get_payload_path("nomenclature", "create_nomenclature.json")
    payload = load_payload(payload_path)
    create_endpoint.new_object(payload=payload, headers=auth_headers)
    nomenclature_id = create_endpoint.response_json["id"]
    assert create_endpoint.check_response_code_is_(201)

    delete_endpoint = DeleteNomenclature()
    delete_endpoint.delete_object(nomenclature_id=nomenclature_id, headers=auth_headers)
    # assert delete_endpoint.check_response_code_is_(200)

    get_by_id_endpoint = GetByIdNomenclature()
    get_by_id_endpoint.get_by_id_object(nomenclature_id=nomenclature_id, headers=auth_headers)
    assert get_by_id_endpoint.check_response_code_is_(404)
