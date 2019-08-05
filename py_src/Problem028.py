# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral 
# is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

import logging
import numpy

# logging.basicConfig(filename="sample.log", level=logging.INFO)
logging.basicConfig(level=logging.INFO)


class Problem028():

	def fillbystep(self, i, count, step, x):
		for k in range(i):
			count += 1
			x += step
			self.iMatrix[x] = count
		return x, count

	def SpiralArr(self, param):
		assert int(param) > 0 and param%2 > 0, "Вводимые данные должны быть нечетными числами больше 0 и целыми!!!"

		matrix = [0 for x in range(param**2)]
		count = 1
		d_sum1 = 0
		d_sum2 = 0
		sum_of_d = 0
		x = int(len(matrix)/2) #центральный индекс одномерного массива
		matrix[x] = count
		logger = logging.getLogger("FindDiagonalSum")
		logger.info('start')
		step1 = 1
		step2 = param
		step3 = -1
		step4 = -param
		self.iMatrix = matrix

		for i in range(1, param+1):
			if i < param and i%2 > 0: 
				x, count = self.fillbystep(i, count, step1, x)
				x, count = self.fillbystep(i, count, step2, x)
			if i < param and i%2 == 0:
				x, count = self.fillbystep(i, count, step3, x)
				x, count = self.fillbystep(i, count, step4, x)
			if i == param:
				if count < param**2:
					x, count = self.fillbystep(i-1, count, step1, x)
				if count < param**2:
					x, count = self.fillbystep(i-1, count, step2, x)
			matrix = self.iMatrix
			# alex
			# for i in range(1, param+1):
			# 	if i < param and i%2 > 0: 
			# 		for k in range(i):
			# 			count += 1
			# 			x += step1
			# 			matrix[x] = count 
			# 			# print(" x = " + str(x) + " matrix[x] = " + str(matrix[x]))
			# 		for n in range(i):	
			# 			count += 1
			# 			x += step2
			# 			matrix[x] = count
			# 			# print(" x = " + str(x) + " matrix[x] = " + str(matrix[x]))
			# 	if i < param and i%2 == 0:
			# 		for k in range(i):
			# 			count += 1
			# 			x += step3
			# 			matrix[x] = count
			# 			# print("по 2 шага  x = " + str(x) + " matrix[x] = " + str(matrix[x]))
			# 		for n in range(i):
			# 			count += 1
			# 			x += step4
			# 			matrix[x] = count
			# 			# print("по 2 шагаx = " + str(x) + " matrix[x] = " + str(matrix[x]))
			# 	if i == param:
			# 		print("i = " + str(i))
			# 		for k in range(i-1):
			# 			if count < param**2:
			# 				count += 1
			# 				x += step1
			# 				matrix[x] = count 
			# 				# print(" x = " + str(x) + " matrix[x] = " + str(matrix[x]))
			# 		for n in range(i-1):
			# 			if count < param**2:	
			# 				count += 1
			# 				x += step2
			# 				matrix[x] = count	
		
		logger.info(str(matrix))
		new_matrix = numpy.array(matrix).reshape(-1, param)
		# logger.info(str(new_matrix))
		for x in range(param):
			if x != int(param/2):
				d_sum1 += new_matrix[x][x]
				# print(new_matrix[x][x])
			for y in range(param-1, 0, -1):
				d_sum2 += new_matrix[y-x][x]
				# print(new_matrix[y-x][x])
				break
		sum_of_d = d_sum1 + d_sum2
		print(new_matrix)

		return sum_of_d


	# def SumOfDiagonals(self, matrix):


if __name__ == "__main__":
	n = Problem028()
	print(n.SpiralArr(5))