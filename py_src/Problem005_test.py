import unittest
import Problem005

class DivWithoutRemainderTest(unittest.TestCase):
	def testSmalestNumb(self):
		p = Problem005.DivWithoutRemainder()
		self.assertEqual(p.SmalestNumb(1, 10), 2520)
        
if __name__ == '__main__':
    unittest.main()