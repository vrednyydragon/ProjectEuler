import unittest
import Problem012
#from Problem021 import AmicableNumbers

class TriangleNumbersTest(unittest.TestCase):
	def testgetNumForDivCnt(self):
		p = Problem012.TriangleNumbers()
		self.assertEqual(p.getNumForDivCnt(6), (28, [28.0, 14.0, 7.0, 4.0, 2.0, 1.0]))



if __name__ == '__main__':
    unittest.main()