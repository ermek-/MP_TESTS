from endpoints.nomenclature.create import CreateNomenclature
from endpoints.nomenclature.delete import DeleteNomenclature
from endpoints.nomenclature.update import UpdateNomenclature
from endpoints.production_order.create import CreateOrder
from endpoints.production_order.update import UpdateOrder
from endpoints.production_order.delete import DeleteOrder
from tests.payload_utils import load_payload, get_payload_path

def test_update_nomenclature(auth_headers):
    create_endpoint = CreateNomenclature()
    payload_path = get_payload_path("nomenclature", "create_nomenclature.json")
    payload = load_payload(payload_path)
    create_endpoint.new_object(payload=payload, headers=auth_headers)
    nomenclature_id = create_endpoint.response_json["id"]
    assert create_endpoint.check_response_code_is_(201)

    update_endpoint = UpdateNomenclature()
    payload_path = get_payload_path("nomenclature", "create_nomenclature.json")
    payload = load_payload(payload_path)
    update_endpoint.update_object(payload=payload, headers=auth_headers, nomenclature_id=nomenclature_id)
    # assert update_endpoint.check_response_code_is_(200)

    delete_endpoint = DeleteNomenclature()
    delete_endpoint.delete_object(nomenclature_id=nomenclature_id, headers=auth_headers)
    # assert delete_endpoint.check_response_code_is_(200)
