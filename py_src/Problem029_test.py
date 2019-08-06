import unittest
import Problem029

class Problem028Test(unittest.TestCase):
	def testSpiralArr(self):
		p = Problem029.Problem029()
		self.assertEqual(p.DistinctPowers(2, 5), (15))

if __name__ == '__main__':
    unittest.main()