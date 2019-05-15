import unittest
import Problem020

class FactorialTest(unittest.TestCase):
	def testSumOfDigits(self):
		p = Problem020.Factorial()
		self.assertEqual(p.SumOfDigits(10), 27)
		# self.assertEqual(Problem017.NumbersIntoWords.HowManyLetters(Problem017.NumbersIntoWords(), 5), 19)

if __name__ == '__main__':
    unittest.main()