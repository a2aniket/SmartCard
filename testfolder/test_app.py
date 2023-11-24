from app import *
import unittest
from flask import Flask,render_template,request
import pickle
import pandas as pd  

class TestBill(unittest.TestCase):
    def test_total_price(self):
        with open('bill.pkl', 'rb') as handle:
            b = pickle.load(handle)
        total=0
        for i in b:
            total=total+b[i]['totalPrice']
        self.assertTrue(isinstance(total, float))
    
    def test_unit_count(self):
        with open('bill.pkl', 'rb') as handle:
            b = pickle.load(handle)
        units=0
        for i in b:
            units=units+b[i]['unit']
        self.assertTrue(isinstance(units, int))
    
    def test_home_page(self):
        app = Flask(__name__)
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
    
    def test_home_page_content(self):
        app = Flask(__name__)
        with app.test_client() as client:
            response = client.get('/')
            self.assertIn(b'bill', response.data)
            self.assertIn(b'units', response.data)
            self.assertIn(b'total', response.data)

if __name__ == '__main__':
    unittest.main()