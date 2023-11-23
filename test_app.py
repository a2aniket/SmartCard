from app import *
import unittest
from flask import Flask, render_template, request
import pickle
import pandas as pd

class TestHome(unittest.TestCase):
    
    def test_home(self):
        with open('bill.pkl', 'rb') as handle:
            b = pickle.load(handle)
        total = 0
        units = 0
        for i in b:
            total = total + b[i]['totalPrice']
            units = units + b[i]['unit']
        result = render_template("home.html",bill=b,units=units,total=total)
        self.assertIsNotNone(result)
    
    def test_home_with_empty_bill(self):
        b = {}
        total = 0
        units = 0
        for i in b:
            total = total + b[i]['totalPrice']
            units = units + b[i]['unit']
        result = render_template("home.html",bill=b,units=units,total=total)
        self.assertIsNotNone(result)
    
    def test_home_with_invalid_file_name(self):
        with self.assertRaises(FileNotFoundError):
            with open('invalid_bill.pkl', 'rb') as handle:
                b = pickle.load(handle)
    
    def test_home_with_invalid_file_format(self):
        with open('bill.txt', 'rb') as handle:
            with self.assertRaises(pickle.UnpicklingError):
                b = pickle.load(handle)
    
    def test_home_with_invalid_template_name(self):
        with self.assertRaises(TemplateNotFound):
            result = render_template("invalid_home.html",bill={},units=0,total=0)
    
    def test_home_with_invalid_data_type(self):
        with self.assertRaises(TypeError):
            result = render_template("home.html",bill=[],units=0,total=0)

if __name__ == "__main__":
    unittest.main()