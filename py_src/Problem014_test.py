import unittest
import Problem014

class SequenceTest(unittest.TestCase):
	def testMaxSequence(self):
		p = Problem014.Sequence()
		self.assertEqual(p.MaxSequence(13), (20, 9) )
        
if __name__ == '__main__':
    unittest.main()