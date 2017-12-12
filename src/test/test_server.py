import falcon
from falcon import testing
from faker import Faker


from src.server.server import myapp
from src.client.client import get_request

class MainTestCase(testing.TestCase):
    def setUp(self):
        super(MainTestCase, self).setUp()
        self.app = myapp()


class ServerTestCase(MainTestCase):
    def test_server_returns_correct_size(self):
        fake = Faker()
        test_body = fake.text()
        size = len(test_body)
        expected_result = {
            'received_bytes': size
        }
        result = self.simulate_post('/', body=test_body)
        self.assertEqual(result.json, expected_result)
