import unittest
import Problem059

class Problem059Test(unittest.TestCase):
	def testSpiralArr(self):
		p = Problem059.Problem059()
		self.assertEqual(p.XOR_Decryption('p059_cipher.txt'), (129448))

if __name__ == '__main__':
    unittest.main()