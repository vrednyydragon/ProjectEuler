import unittest
import Problem054

class Problem054Test(unittest.TestCase):
	def testSpiralArr(self):
		p = Problem054.Problem054()
		self.assertEqual(p.PokerHands('p054_poker.txt'), 376)

if __name__ == '__main__':
    unittest.main()