from app import *
import unittest
import pickle
from app import app
from flask import Flask

class TestBill(unittest.TestCase):

    def test_home(self):
        with app.test_client() as c:
            response = c.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'text/html; charset=utf-8')

    def test_bill_data(self):
        with open('bill.pkl', 'rb') as handle:
            b = pickle.load(handle)
        self.assertIsNotNone(b)

    def test_bill_total(self):
        with open('bill.pkl', 'rb') as handle:
            b = pickle.load(handle)
        total = 0
        for i in b:
            total = total + b[i]['totalPrice']
        self.assertIsNotNone(total)

    def test_bill_units(self):
        with open('bill.pkl', 'rb') as handle:
            b = pickle.load(handle)
        units = 0
        for i in b:
            units = units + b[i]['unit']
        self.assertIsNotNone(units)

if __name__ == '__main__':
    unittest.main()