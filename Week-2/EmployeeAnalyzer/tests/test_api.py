import requests
import unittest
from unittest.mock import patch, Mock

NATIONALIZE_API_URL = "https://api.nationalize.io"

def load_data(emp_name):
    response = requests.get(NATIONALIZE_API_URL,params={"name": emp_name},timeout=5)
    response.raise_for_status()
    data = response.json()
    return data

# Class
class TestGetData(unittest.TestCase):
    @patch('requests.get')
    def test_get_data(self, mock_get_data):
        mock_data =  {'count': 200018, 'name': 'Raj', 'country': [{'country_id': 'IN', 'probability': 0.41083}, {'country_id': 'SA', 'probability': 0.081486}, {'country_id': 'QA', 'probability': 0.051763}, {'country_id': 'US', 'probability': 0.044113}, {'country_id': 'GB', 'probability': 0.040897}]}
        mock_get_data.return_value = Mock()

        mock_get_data.return_value.json.return_value = mock_data
        mock_get_data.return_value.status_code = 200

        result = load_data("Raj")

        self.assertEqual(result, mock_data)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
