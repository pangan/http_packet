from falcon import testing
from faker import Faker
import json

from src.server.server import myapp


class MainTestCase(testing.TestCase):
    def setUp(self):
        super(MainTestCase, self).setUp()
        self.app = myapp()


class ServerTestCase(MainTestCase):
    def test_server_returns_correct_size(self):
        fake = Faker()
        test_body = fake.text()
        data_json = {'a':test_body}
        size = len(json.dumps(data_json))
        json_value_size = len(test_body)
        expected_result = {
            'received_bytes': size,
            'received_json_value_size': json_value_size
        }
        headers = {"Content-Type": "application/json"}
        result = self.simulate_post('/', body=json.dumps(data_json), headers=headers)
        self.assertEqual(result.json, expected_result)
