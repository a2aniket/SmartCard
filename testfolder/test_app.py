from app import *
import unittest
from flask import Flask

class TestHome(unittest.TestCase):
    def test_home(self):
        app = Flask(__name__)
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'text/html; charset=utf-8')
    
    def test_pkl_file(self):
        with open('bill.pkl', 'rb') as handle:
            b = pickle.load(handle)
        self.assertIsInstance(b, dict)
    
    def test_total_price(self):
        with open('bill.pkl', 'rb') as handle:
            b = pickle.load(handle)
        total=0
        for i in b:
            total=total+b[i]['totalPrice']
        self.assertIsInstance(total, float)
    
    def test_units(self):
        with open('bill.pkl', 'rb') as handle:
            b = pickle.load(handle)
        units=0
        for i in b:
            units=units+b[i]['unit']
        self.assertIsInstance(units, int)
    
if __name__ == '__main__':
    unittest.main()