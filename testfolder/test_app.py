from app import *
import unittest
from flask import Flask, render_template, request
import pickle
import pandas as pd

class TestHome(unittest.TestCase):

    def test_home(self):
        app = Flask(__name__)
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
    
    def test_bill(self):
        with open('bill.pkl', 'rb') as handle:
            b = pickle.load(handle)
        self.assertIsInstance(b, dict)
        
    def test_total(self):
        with open('bill.pkl', 'rb') as handle:
            b = pickle.load(handle)
        total = 0
        for i in b:
            total = total + b[i]['totalPrice']
        self.assertIsInstance(total, float)
        
    def test_units(self):
        with open('bill.pkl', 'rb') as handle:
            b = pickle.load(handle)
        units = 0
        for i in b:
            units = units + b[i]['unit']
        self.assertIsInstance(units, int)

if __name__ == '__main__':
    unittest.main()