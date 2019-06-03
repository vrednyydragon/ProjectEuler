import unittest
import Problem023

class SumOfNumbersTest(unittest.TestCase):
	def testFindDivisors(self):
		p = Problem023.SumOfNumbers()
		self.assertEqual(p.SumOfPositiveNumb(24), (276))



if __name__ == '__main__':
    unittest.main()