import unittest
import Problem002

class FibonacciTest(unittest.TestCase):
	def test_Fibonacci_sum_of_even_numbers(self):
		p = Problem002.Fibonacci()
		self.assertEqual(p.Fibonacci_sum_of_even_numbers(10), 44)
        
if __name__ == '__main__':
    unittest.main()