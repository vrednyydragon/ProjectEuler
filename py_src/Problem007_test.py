import unittest
import Problem007

class PrimeNumbersTest(unittest.TestCase):
	def testFindPrimeNumber(self):
		p = Problem007.PrimeNumbers()
		self.assertEqual(p.FindPrimeNumber(6), 13 )
        
if __name__ == '__main__':
    unittest.main()