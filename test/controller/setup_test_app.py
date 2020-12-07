from unittest import TestCase
from src.app import app


class TestAppClient(TestCase):

    def create_app(self):
        new_app = app
        new_app.config["TESTING"] = True
        new_app.config["DEBUG"] = True
        new_app.testing = True
        new_app.debug = True
        return new_app
