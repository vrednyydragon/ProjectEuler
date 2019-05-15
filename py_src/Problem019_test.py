import unittest
import Problem019

class DaysYearsTest(unittest.TestCase):
	def testWhatDay(self):
		p = Problem019.DaysYears()
		self.assertEqual(p.WhatDay(1901, 2001, 7), 171)
		# self.assertEqual(Problem017.NumbersIntoWords.HowManyLetters(Problem017.NumbersIntoWords(), 5), 19)

if __name__ == '__main__':
    unittest.main()