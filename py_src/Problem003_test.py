import unittest
import Problem003

class PrimeFactorsTest(unittest.TestCase):
	def testPrimeFactorsMaxNumber(self):
		p = Problem003.PrimeFactors()
		self.assertEqual(p.PrimeFactorsMaxNumber(13195), 29)
        
if __name__ == '__main__':
    unittest.main()