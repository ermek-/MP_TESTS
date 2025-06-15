from endpoints.production_order.get_by_id import GetByIdOrder

def test_get_by_id_production_order(auth_headers):
    endpoint = GetByIdOrder()
    endpoint.get_by_id_object(order_id=27,headers=auth_headers)