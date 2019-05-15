import unittest
import Problem001_2

class SumTest(unittest.TestCase):
	def test_SumMultiplues(self):
		p = Problem001_2.Sum()
		self.assertEqual(p.SumMultiplues(10), 23)
        
if __name__ == '__main__':
    unittest.main()