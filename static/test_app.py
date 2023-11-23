from app import *
import unittest
from flask import Flask, render_template, request
import pickle

class TestHome(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        with open('bill.pkl', 'rb') as handle:
            self.b = pickle.load(handle)

    def tearDown(self):
        self.app_context.pop()

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_total(self):
        total = 0
        for i in self.b:
            total += self.b[i]['totalPrice']
        response = self.client.get('/')
        self.assertIn(f'Total: {total}', response.get_data(as_text=True))

    def test_home_units(self):
        units = 0
        for i in self.b:
            units += self.b[i]['unit']
        response = self.client.get('/')
        self.assertIn(f'Units: {units}', response.get_data(as_text=True))

    def test_home_bill(self):
        response = self.client.get('/')
        for i in self.b:
            self.assertIn(i, response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()