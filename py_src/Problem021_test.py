import unittest
import Problem021
#from Problem021 import AmicableNumbers

class AmicableNumbersTest(unittest.TestCase):
	def testFindDivisors(self):
		p = Problem021.AmicableNumbers()
		self.assertEqual(p.FindDivisors(220), (220, 284))
		# self.assertEqual(Problem017.NumbersIntoWords.HowManyLetters(Problem017.NumbersIntoWords(), 5), 19)
		#p = AmicableNumbers()
	# def testFindDivisors2(self):
	# 	# p = Problem021.AmicableNumbers()
	# 	self.assertEqual(Problem021.AmicableNumbers().FindDivisors(220), (220, 284))
	# 	# self.assertEqual(Problem017.NumbersIntoWords.HowManyLetters(Problem017.NumbersIntoWords(), 5), 19)
	# 	#p = AmicableNumbers()


if __name__ == '__main__':
    unittest.main()