import unittest
import Problem006

class SquareFunctionsTest(unittest.TestCase):
	def testDifferenceBetweenSumOfSquares(self):
		p = Problem006.SquareFunctions()
		self.assertEqual(p.DifferenceBetweenSumOfSquares(1, 10), 2640 )
        
if __name__ == '__main__':
    unittest.main()