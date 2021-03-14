import unittest
from unittest.mock import patch
import app2
from flask import request

def test_index(self):
    with patch('index.request.post') as mocked_method:
        mocked_method.return_value = 'True'
        result = self.index()
        mocked_method.assert_called_with('ankit', '1234','app@gmail.com', '2')
        self.assertEqual(result, 'success')
