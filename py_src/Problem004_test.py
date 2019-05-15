import unittest
import Problem004

class PalindromeTest(unittest.TestCase):
	def testLargestPalindrome(self):
		p = Problem004.Palindrome()
		self.assertEqual(p.LargestPalindrome(2), str(9009))
		# self.assertEqual(Problem004.Palindrome.LargestPalindrome(2), '9009') так тоже работает
        
if __name__ == '__main__':
    unittest.main()