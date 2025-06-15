from endpoints.production_order.get import GetOrder

def test_get_production_order(auth_headers):
    endpoint = GetOrder()
    endpoint.get_object(headers=auth_headers)