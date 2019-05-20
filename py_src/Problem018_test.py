import unittest
import Problem018

class SumInTriangleTest(unittest.TestCase):
	def testMaximumPathSum(self):
		p = Problem018.SumInTriangle()
		a = ["3",
			"7 4",
			"2 4 6",
			"8 5 9 3"]
		self.assertEqual(p.MaximumPathSum(a), (23))

if __name__ == '__main__':
    unittest.main()