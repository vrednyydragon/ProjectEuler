# Reciprocal cycles
# A unit fraction contains 1 in the numerator. The decimal representation of the
# unit fractions with denominators 2 to 10 are given:
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
# its decimal fraction part.

import logging
# logging.basicConfig(filename="sample.log", level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

class ReciprocalСycles():

	def FindLongestRecurringCycle(self, input_denom):
		denominator = 2
		unit_fraction = 0
		interval = 1
		max_len = 0

		logger = logging.getLogger("FindLongestRecurringCycle")
		logger.info('start')

		while denominator != (input_denom + 1):
			unit_fraction = 1/denominator
			denominator += 1
			str1 = str(unit_fraction)
			str_fraction = str(unit_fraction)[:0] + str(unit_fraction)[2:]  # в данной строке удаляем '0.'
			logger.debug(str_fraction)
			for i in range(len(str_fraction)-2):
				# while str_fraction(len(str_fraction)-1) == :
				for n in range(1, len(str_fraction)-1):
					if str_fraction[i] != str_fraction[n] and str_fraction[i+1] != str_fraction[n+n]:
						print(str_fraction[i:(n+1)])
					# elif str_fraction[i] == str_fraction[n] or str_fraction[i+1] == str_fraction[n+1]:
					else:
						break

					if len(str_fraction[i:(n+1)]) >	max_len:
						max_len = len(str_fraction[i:(n+1)])
		logger.debug(max_len)

		return max_len

if __name__ == "__main__":
	n = ReciprocalСycles()
	print(n.FindLongestRecurringCycle(10))

