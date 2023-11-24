from app import *
import unittest
from flask import Flask,render_template,request
import pickle
import pandas as pd

class TestHome(unittest.TestCase):
    
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        with open('bill.pkl', 'wb') as f:
            pickle.dump({'item1': {'totalPrice': 100, 'unit': 2}, 'item2': {'totalPrice': 200, 'unit': 3}}, f)
    
    def tearDown(self):
        pass
    
    def test_home(self):
        with self.app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Total Price: 300', response.data)
            self.assertIn(b'Units: 5', response.data)
            self.assertIn(b'item1', response.data)
            self.assertIn(b'item2', response.data)
    
    def test_home_empty(self):
        with self.app.test_client() as client:
            with open('bill.pkl', 'wb') as f:
                pickle.dump({}, f)
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Total Price: 0', response.data)
            self.assertIn(b'Units: 0', response.data)
    
    def test_home_single_item(self):
        with self.app.test_client() as client:
            with open('bill.pkl', 'wb') as f:
                pickle.dump({'item1': {'totalPrice': 100, 'unit': 2}}, f)
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Total Price: 100', response.data)
            self.assertIn(b'Units: 2', response.data)
            self.assertIn(b'item1', response.data)
    
    def test_home_multiple_items(self):
        with self.app.test_client() as client:
            with open('bill.pkl', 'wb') as f:
                pickle.dump({'item1': {'totalPrice': 100, 'unit': 2}, 'item2': {'totalPrice': 200, 'unit': 3}, 'item3': {'totalPrice': 50, 'unit': 1}}, f)
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Total Price: 350', response.data)
            self.assertIn(b'Units: 6', response.data)
            self.assertIn(b'item1', response.data)
            self.assertIn(b'item2', response.data)
            self.assertIn(b'item3', response.data)

if __name__ == '__main__':
    unittest.main()