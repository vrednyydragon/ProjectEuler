import unittest
import Problem024

class LexicographicPermutationsTest(unittest.TestCase):
	def testNumberPermutation(self):
		p = Problem024.LexicographicPermutations()
		self.assertEqual(p.NumberPermutation('012', 4), ('120'))

if __name__ == '__main__':
    unittest.main()