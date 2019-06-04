# Lexicographic permutations
# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it
# lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
from itertools import permutations
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO)

class LexicographicPermutations():

	def NumberPermutation(self, arr_numbers, perm_numb):

		logger = logging.getLogger("NumberPermutation")
		permut = [''.join(p) for p in permutations(arr_numbers)]
		logger.info(str(permut))
		logger.info(str(len(permut)))
		# print(permut)
		# print(len(permut))
		return permut[perm_numb-1]
if __name__ == "__main__":
	n = LexicographicPermutations()
	# arr1 = [0, 1, 2]
	# arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	# arr1 = '012'
	arr1 = '0123456789'

	print(n.NumberPermutation(arr1, 1000000))