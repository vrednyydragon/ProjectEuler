# Non-abundant sums
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the
#  number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is
#  called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can
#  be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown
#  that all integers greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though it is
# known that the greatest number that cannot be expressed as the sum of two abundant numbers is
# less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant
# numbers.
import logging

logging.basicConfig(filename="sample.log", level=logging.DEBUG)

class SumOfNumbers():

	def AbundantNumber(self, input_data):

		logger = logging.getLogger("AbundantNumber")
		logger.info("Start1")
		numbers = input_data
		ab_number = 0
		sum_all_num = 0
		arr_ab_number = []

		for i in range (1, numbers+1):
			sum_all_num = 0
			for k in range(1, numbers+1):
				if i%k == 0 and i/k != i:
					# logger.info(str(i) + " - " + str(int(i/k)))
					# print(i, int(i/k))
					sum_all_num += i/k
					# print(int(sum_all_num))
			if sum_all_num > i:
				ab_number = i
				# print(ab_number)
				arr_ab_number.append(ab_number)
				# print(arr_ab_number)
		return arr_ab_number

	def SumOfTwoAbundantNumb(self, input_data):
		logging.info("Start2")
		sum_two_numb = []
		arr_ab_number = self.AbundantNumber(input_data)
		for i in arr_ab_number:
			for k in arr_ab_number:
				sum_two_numb.append(i + k)
		return sum_two_numb

	def SumOfPositiveNumb(self, input_data):
		logging.info("Start3")
		sum_of_numb = 0
		for i in range(1, input_data):
			if i not in self.SumOfTwoAbundantNumb(input_data):
				sum_of_numb += i
		return sum_of_numb

if __name__ == "__main__":
	n = SumOfNumbers()
	# print(n.AbundantNumber(100))
	# print(n.SumOfTwoAbundantNumb(100))
	print(n.SumOfPositiveNumb(1000))