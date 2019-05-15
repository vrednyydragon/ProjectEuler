class DivWithoutRemainder():
	
	def SmalestNumb(self, input_data1, input_data2):
		assert 0 < int(input_data1) < int(input_data2), "Вводимые данные должны быть числами больше 0, целыми, при чем a < b !!!" 
		small_numb = 0
		lowerD = int(input_data1)
		maxD = int(input_data2)
		flag = False
		while(not flag):
			small_numb += 1
			for i in range(lowerD, maxD+1, 1):
				if (small_numb%i!=0):
					break
				if (i == maxD):
					flag = True
		print( " the smallest positive number :" + str(small_numb))
		return small_numb

if __name__ == "__main__":
	a = input("введите число a: ")
	b = input("введите число b: ")
	n = DivWithoutRemainder()
	print(n.SmalestNumb(a, b))
	# так делать не надо!
	# assert 0 < int(a) < int(b)
	# assert False, "Вводимые данные должны быть числами больше 0, целыми, при чем a < b !!!"
	#print(DivWithoutRemainder.SmalestNumb(1, 10))


	