from endpoints.nomenclature.create import CreateNomenclature
from endpoints.nomenclature.create_batch import CreateBatchNomenclature
from endpoints.nomenclature.delete import DeleteNomenclature
from tests.payload_utils import load_payload, get_payload_path

def test_create_nomenclature(auth_headers):
    create_endpoint = CreateNomenclature()
    payload_path = get_payload_path("nomenclature", "create_nomenclature.json")
    payload = load_payload(payload_path)
    create_endpoint.new_object(headers=auth_headers, payload=payload)
    nomenclature_id = create_endpoint.response_json["id"]

    endpoint = CreateBatchNomenclature()
    payload_path = get_payload_path("nomenclature", "create_nomenclature_batch.json")
    payload = load_payload(payload_path)
    endpoint.new_object(headers=auth_headers, payload=payload, nomenclature_id=nomenclature_id)
    assert endpoint.check_response_code_is_(201)
    assert endpoint.check_count(777)

    delete_endpoint = DeleteNomenclature()
    delete_endpoint.delete_object(nomenclature_id=nomenclature_id, headers=auth_headers)
    # assert delete_endpoint.check_response_code_is_(200)
