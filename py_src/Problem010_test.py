import unittest
import Problem010

class PrimeNumbersTest(unittest.TestCase):
	def testSumPrimeNumber(self):
		p = Problem010.PrimeNumbers()
		self.assertEqual(p.SumPrimeNumber(10), 17 )
        
if __name__ == '__main__':
    unittest.main()