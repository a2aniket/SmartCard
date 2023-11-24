from app import *
import unittest
from app import app

class TestHome(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_template_used(self):
        response = self.client.get('/')
        self.assert_template_used('home.html')

    def test_home_total_price(self):
        with open('bill.pkl', 'rb') as handle:
            b = pickle.load(handle)
        total = 0
        for i in b:
            total += b[i]['totalPrice']
        response = self.client.get('/')
        self.assertIn(str(total), response.get_data(as_text=True))

    def test_home_unit_count(self):
        with open('bill.pkl', 'rb') as handle:
            b = pickle.load(handle)
        units = 0
        for i in b:
            units += b[i]['unit']
        response = self.client.get('/')
        self.assertIn(str(units), response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()