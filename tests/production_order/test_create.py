from endpoints.production_order.create import CreateOrder

def test_create_production_order(auth_headers):
    endpoint = CreateOrder()
    payload = {
  "number": "payment_kazakhstan.flx",
  "date_get": "2025-05-26",
  "required_date": "2025-05-26",
  "date_complite": "2025-05-26",
  "priority": 455,
  "customer": "Nichole21",
  "client_order": 1,
  "description": "6832 Stefanie Station",
  "avaible_quantity": "Toy",
  "ready_persent": 101
}
    endpoint.new_object(payload=payload, headers=auth_headers)
    endpoint.check_number(payload['number'])


