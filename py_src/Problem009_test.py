import unittest
import Problem009

class PythagoreanTripletTest(unittest.TestCase):
	def testFindPythagoreanTriplet(self):
		p = Problem009.PythagoreanTriplet()
		self.assertEqual(p.FindPythagoreanTriplet(12), (3, 4, 5))
        
if __name__ == '__main__':
    unittest.main()