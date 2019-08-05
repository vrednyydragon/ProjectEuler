import unittest
import Problem028

class Problem028Test(unittest.TestCase):
	def testSpiralArr(self):
		p = Problem028.Problem028()
		self.assertEqual(p.SpiralArr(5), (101))

if __name__ == '__main__':
    unittest.main()