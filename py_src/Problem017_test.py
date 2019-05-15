import unittest
import Problem017

class NumbersIntoWordsTest(unittest.TestCase):
	def testHowManyLetters(self):
		p = Problem017.NumbersIntoWords()
		self.assertEqual(p.HowManyLetters(5), 19)
		# self.assertEqual(Problem017.NumbersIntoWords.HowManyLetters(Problem017.NumbersIntoWords(), 5), 19)

if __name__ == '__main__':
    unittest.main()