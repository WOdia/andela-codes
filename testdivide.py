import unittest
from divide import divide_two_numbers
class TestMyFunc(unittest.TestCase):

	def test_basic_division(self):
		self.assertEqual(divide_two_numbers(10,2),5,msg="Test failed")
	def test_one_negative(self):
		self.assertEqual(divide_two_numbers(-20,2),-10)
	def test_two_negatives(self):
		self.assertEqual(divide_two_numbers(-30,-3),10)
	def test_float_answers(self):
		self.assertEqual(divide_two_numbers(5,2),2.5)

     




if __name__=='__main__':
	unittest.main()