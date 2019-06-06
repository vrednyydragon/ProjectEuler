import unittest
import Problem025

class FibonacciTest(unittest.TestCase):
	def testNumberPermutation(self):
		p = Problem025.Fibonacci()
		self.assertEqual(p.FindIndex(3), (12))

if __name__ == '__main__':
    unittest.main()