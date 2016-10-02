import os
from getgauge.python import Messages
import requests

class MobileAppClient(object):
    def __init__(self, email="", username="", authzn_code=None, access_token=None):
        """Create a REST Client to simulate a mobile app."""
        self.email = email
        self.username = username
        self.access_token = access_token
        self.authzn_code = authzn_code
        self.cart_id = ""
        self.order_id = ""

    def get_order_id(self):
        return self.order_id

    def _getBaseUrl(self):
        return os.getenv('MAGENTO_URL')

    def _getHeaders(self):
        headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json'
        }
        if self.access_token is not None:
            headers['Authorization'] = "Bearer " + self.access_token
        return headers

    def _apiRequest(self, method, endpoint, jsonObj=None):
        baseurl = self._getBaseUrl()
        url = baseurl + endpoint
        headers = self._getHeaders()

        req = requests.Request(method=method, url=url, params=None, json=jsonObj, headers=headers)
        prepared = req.prepare()
        self._log_request(prepared)

        s = requests.Session()
        response = s.send(prepared, verify=False)
        self._log_response(response)

        return response

    def _log_request(self, req):
        Messages.write_message('\n<b>{} {}</b>'.format(req.method, req.url))
        Messages.write_message('\n<i>Request Headers:</i>')
        Messages.write_message('\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()))
        Messages.write_message('\n<i>Request Body:</i>')
        Messages.write_message('{}'.format(req.body))

    def _log_response(self, res):
        Messages.write_message('\n---Response---')
        Messages.write_message('<i>Status code:</i> <b>{}</b>'.format(res.status_code))
        Messages.write_message('\n<i>Response Headers:</i>')
        Messages.write_message('\n'.join('{}: {}'.format(k, v) for k, v in res.headers.items()))
        if res.status_code != requests.codes.no_content:
            Messages.write_message('\n<i>Response Body:</i>')
            Messages.write_message('{}'.format(res.json()))

    def request_token(self, password):
        json = {'username': self.email, 'password': password}
        response = self._apiRequest(method='POST', endpoint='/index.php/rest/V1/integration/customer/token', jsonObj=json)
        json = response.json()
        self.access_token = json

    def create_cart(self):
        response = self._apiRequest(method='POST', endpoint='/rest/V1/carts/mine')
        json = response.json()
        self.cart_id = json

    def add_item_to_cart(self, sku):
        json = {"cart_item": {"quote_id": self.cart_id,"sku": sku,"qty": 1}}
        response = self._apiRequest(method='POST', endpoint='/rest/V1/carts/mine/items', jsonObj=json)

    def set_shipping_info(self, email, firstname, lastname, street, city, region, postcode, country, telephone):
        json = {
                  "addressInformation": {
                    "shipping_address": {
                      "region": region,
                      "region_id": 0,
                      "region_code": "AUS",
                      "country_id": country,
                      "street": [
                        street
                      ],
                      "telephone": telephone,
                      "postcode": postcode,
                      "city": city,
                      "firstname": firstname,
                      "lastname": lastname,
                      "email": email,
                      "same_as_billing": 1
                    },
                    "shipping_method_code": "flatrate",
                    "shipping_carrier_code": "flatrate"
                  }
                }

        response = self._apiRequest(method='POST', endpoint='/rest/V1/carts/mine/shipping-information', jsonObj=json)

    def submit_cart_payment_info(self, email, firstname, lastname, street, city, region, postcode, country, telephone):
        json = {
            "paymentMethod": {
                "method": "checkmo",
            },
            "billingAddress": {
                "region": region,
                "region_id": 0,
                "region_code": "AUS",
                "country_id": country,
                "street": [
                    street
                ],
                "telephone": telephone,
                "postcode": postcode,
                "city": city,
                "firstname": firstname,
                "lastname": lastname,
                "email": email
            }
        }

        response = self._apiRequest(method='POST', endpoint='/rest/V1/carts/mine/payment-information', jsonObj=json)
        self.order_id = response.json()

    def get_cart_payment_info(self):
        response = self._apiRequest(method='GET',endpoint='/rest/V1/carts/mine/payment-information' )
        json = response.json()
        return json

