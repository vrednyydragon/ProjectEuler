import unittest
import Problem008

class AdjacentDigitsTest(unittest.TestCase):
	def testMultiplyAdjacentDigits(self):
		p = Problem008.AdjacentDigits()
		self.assertEqual(p.MultiplyAdjacentDigits(4), 5832)
        
if __name__ == '__main__':
    unittest.main()