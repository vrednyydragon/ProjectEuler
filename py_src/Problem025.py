# 1000-digit Fibonacci number
# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# ....
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import logging
# logging.basicConfig(filename="sample.log", level=logging.INFO)
logging.basicConfig(level=logging.INFO)

class Fibonacci():

	def FindIndex(self, digits):
		f1 = 1
		f2 = 1
		f3 = 0
		index = 2
		logger = logging.getLogger("FindIndex")
		logger.info('start')
		while len(str(f3)) != digits:
			f3 = f1 + f2
			f1 = f2
			f2 = f3
			index += 1
		logger.info(str(f3))
		logger.info(str(index))

		return index
if __name__ == "__main__":
	n = Fibonacci()
	print(n.FindIndex(1000))