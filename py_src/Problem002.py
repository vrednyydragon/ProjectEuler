class Fibonacci():
	
	def Fibonacci_sum_of_even_numbers(self, input_data):
		assert 0 < int(input_data), "Вводимые данные должны быть числами больше 0 числами и целыми!!!"
		numb = int(input_data)
		n0 = 1
		n1 = 1
		n2 = 0
		sum_=0

		for i in range (3, numb):
			n2=n0+n1
			n0=n1
			n1=n2
			if ((n2%2)==0):
				sum_+=n2
				print("Четное число: "+ str(n2))
		print("Сумма четных чисел: "+ str(sum_))
		return sum_

if __name__ == "__main__":
	n = Fibonacci()
	print(n.Fibonacci_sum_of_even_numbers(10))