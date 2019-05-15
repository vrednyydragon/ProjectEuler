import unittest
import Problem016

class DegreeTest(unittest.TestCase):
	def testSumOfDigits(self):
		p = Problem016.Degree()
		self.assertEqual(p.SumOfDigits(15), 26 )
        
if __name__ == '__main__':
    unittest.main()