class PythagoreanTriplet():

	def FindPythagoreanTriplet(self, input_data):
		assert 0 < int(input_data), "Вводимые данные должны быть числами больше 0 числами и целыми!!!"
		a = 0
		b = 0
		c = 0
		sum_ = 0
		lim = int(input_data)

		for i in range (lim + 1):
			# c += 1
			a = i
			for n in range (lim + 1):
				# b += 1
				b = n
				for k in range (lim + 1):
					# a += 1
					c = k
					# print("a = " + str(a) +" b = "+ str(b) +" c = "+ str(c))
					sum_ = a + b + c
					sqr1 = (a*a)+(b*b)
					sqr2 = c*c
					# print("sum_ = " + str(sum_))
					if ((a < b) and (b < c) and (sqr1 ==sqr2) and (sum_ == lim)):
						print("--------------------------------------------------")
						print("a = " + str(a) +" b = "+ str(b) +" c = "+ str(c))
						print(sum_)
						return a, b, c
				
if __name__ == "__main__":
	n = PythagoreanTriplet()
	print(n.FindPythagoreanTriplet(1000))
