import unittest
from operations_function import SweetOperator

class TestOperatorsView(unittest.TestCase):

    def setUp(self):
        self.operator = SweetOperator()

    def test_view_empty_sweets(self):
        sweets = self.operator.view_sweets()
        self.assertEqual(sweets, [])   # Should be empty list when no sweets are added
