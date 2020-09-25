# project/server/tests/test_config.py


import unittest
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import current_app
from flask_testing import TestCase
from project.server import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['DB_USER'] is 'neo4j')
        self.assertFalse(app.config['DB_URI'] is 'bolt://localhost:7687')
        self.assertFalse(app.config['DB_PASSWORD'] is '123mduar')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['DB_USER'] is 'neo4j')
        self.assertFalse(app.config['DB_URI'] is 'bolt://localhost:7687')
        self.assertFalse(app.config['DB_PASSWORD'] is '123mduar')
        self.assertTrue(app.config['DEBUG'])


if __name__ == '__main__':
    unittest.main()
