import unittest
# from operations_function import SweetOperator

class TestOperatorsAdd(unittest.TestCase):
    
    # def setUp(self):
    #     self.addOperator =  SweetOperator()
        
    def test_add_valid_sweet(self):
        result = self.addOperator.add_sweet(
            id = 1,
            name = "Kaju Katari",
            category = "chocolate",
            price = 50,
            quantity = 10
        )
        
        self.assertEqual(result, "Sweet Added Successfully")
        self.assertEqual(len(self.addOperator.get_sweets()),1)
        


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)