import unittest
import Problem022

class NamesScoresTest(unittest.TestCase):
	def testFindDivisors(self):
		p = Problem022.NamesScores()
		self.assertEqual(p.SortingNames('names.txt', 938), (871198282))



if __name__ == '__main__':
    unittest.main()