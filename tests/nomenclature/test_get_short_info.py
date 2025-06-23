from endpoints.nomenclature.get_short import GetNomenclatureShortInfo
from tests.payload_utils import get_payload_path, load_json

def test_get_nomenclature_short_info(auth_headers):
    endpoint = GetNomenclatureShortInfo()
    endpoint.get_object(headers=auth_headers,params=None)
    assert endpoint.check_response_code_is_(200)

def test_get_nomenclature_short_info_with_prod_process_id(auth_headers):
    endpoint = GetNomenclatureShortInfo()
    endpoint.get_object(headers=auth_headers, params={"prod_process_id": 1})
    assert endpoint.check_response_code_is_(200)
    assert endpoint.all_prod_process_match(1)