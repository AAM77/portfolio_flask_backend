from unittest import TestCase
from test.controller.setup_test_app import TestAppClient


class TestApp(TestCase):
    def setUp(self):
        self.app = TestAppClient().create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        del self.client

    def test_root_route(self):
        response = self.client.get("/")
        response_text = (response.data).decode("utf-8")
        self.assertEqual(200, response.status_code)
        self.assertEqual("Hello World! This is a test.", response_text)
