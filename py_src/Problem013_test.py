import unittest
import Problem013

class SumOfNumbersTest(unittest.TestCase):
	def testFirstTenDigitsOfSum(self):
		p = Problem013.SumOfNumbers()
		self.assertEqual(p.FirstTenDigitsOfSum(10), '5537376230' )
        
if __name__ == '__main__':
    unittest.main()