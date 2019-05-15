class SquareFunctions ():
	
	def SumOfSquares(self, input_data1, input_data2):
		assert int(input_data1) < int(input_data2), "Вводимые данные должны быть числами, целыми, при чем a < b !!!"
		sumSQ = 0
		for i in range(int(input_data1), int(input_data2)+1):
			sumSQ += i*i
		# print("Сумма квадратов чисел от " + str(input_data1) + " до " + str(input_data2) + " равна: " + str(sumSQ))
		return sumSQ

	def SquareOfSum(self, input_data1, input_data2):
		assert int(input_data1) < int(input_data2), "Вводимые данные должны быть числами, целыми, при чем a < b !!!"
		SQsum = 0
		for i in range(int(input_data1), int(input_data2)+1):
			SQsum += i
		# SQsum = (SQsum*SQsum)
		SQsum *= SQsum
		# print("Квадрат суммы чисел от " + str(input_data1) + " до " + str(input_data2) + " равна: " + str(SQsum))
		return SQsum

	def DifferenceBetweenSumOfSquares(self, input_data1, input_data2):

		# sumSQ = int(input_data1)
		# SQsum = int(input_data2)
		# difference = SQsum - sumSQ
		# print(difference)
		# return difference
		return self.SquareOfSum(input_data1, input_data2) - self.SumOfSquares(input_data1, input_data2)  

if __name__ == "__main__":
	a = input("введите число a: ")
	b = input("введите число b: ")
	# SquareFunctions.SumOfSquares(a, b)
	# SquareFunctions.SquareOfSum(a, b)
	#SquareFunctions.DifferenceBetweenSumOfSquares(SquareFunctions.SumOfSquares(a, b), SquareFunctions.SquareOfSum(a, b))
	n = SquareFunctions()
	print(n.DifferenceBetweenSumOfSquares(a, b))
	# print(n.DifferenceBetweenSumOfSquares(1, 10))


