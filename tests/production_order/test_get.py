from endpoints.production_order.get import GetOrder

def test_create_production_order(auth_headers):
    endpoint = GetOrder()
    endpoint.new_object(headers=auth_headers)