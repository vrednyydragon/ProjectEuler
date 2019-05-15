class PrimeNumbers():
	
	def FindPrimeNumber(self, input_data):
		# assert 0 < int(input_data), "Вводимые данные должны быть числами больше 0 числами и целыми!!!"
		simple_numb = [2]
		arrind = 0
		i = 0
		lim = int(input_data)
		
		while(True):
			i += 1
			if (i > 0) and (i%2 > 0):
				for k in range (arrind+1):
					if(i % simple_numb[k] == 0) or (i <= simple_numb[k]):
						break
					if (k == arrind):
						arrind +=1
						simple_numb.append(i)
						break
			if (arrind == lim-1):
				break
		# print(" simple_numb "+ str(simple_numb[lim-1]))
		return	simple_numb[lim-1]
							
if __name__ == "__main__":
	n = PrimeNumbers()
	print(n.FindPrimeNumber(10001))
		