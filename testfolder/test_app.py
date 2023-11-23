from app import *
import unittest
from flask import Flask, render_template, request
import pickle

class TestApp(unittest.TestCase):
    # Test to check if the Flask app is running successfully
    def test_flask_app(self):
        response = app.test_client(self)
        self.assertEqual(response.status_code, 200)
    
    # Test to check if the home page loads successfully
    def test_home_page(self):
        response = app.test_client(self)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)
    
    # Test to check if the bill is loaded successfully
    def test_bill_loaded(self):
        with open('bill.pkl', 'rb') as handle:
            b = pickle.load(handle)
        self.assertIsNotNone(b)
    
    # Test to check if the total price and units are calculated correctly
    def test_total_units_calculation(self):
        with open('bill.pkl', 'rb') as handle:
            b = pickle.load(handle)
        total=0
        units=0
        for i in b:
            total=total+b[i]['totalPrice']
            units=units+b[i]['unit']
        self.assertEqual(total, 100)
        self.assertEqual(units, 10)
        
if __name__ == '__main__':
    unittest.main()