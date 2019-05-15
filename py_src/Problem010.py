class PrimeNumbers():

	def SumPrimeNumber(self, input_data):
		assert 0 < int(input_data), "Вводимые данные должны быть числами больше 0 числами и целыми!!!"
		simple_numb = [2]
		arrind = 0
		sum_ = 0 
		lim = int(input_data)
		for i in range(lim+1):
			if ((i>0) and (i%2>0)):
				# for k in range(arrind+1):
				for k in range(len(simple_numb)):
					#if((i % simple_numb[k] == 0) or (i <= simple_numb[k])):
					if (i <= simple_numb[k]):
						# print("failure")
						break
					if(i % simple_numb[k] == 0):
						break
					elif(k == len(simple_numb)-1):
					# if(k == arrind):
						# print("--------------------------")
						# print(i)
						# print(simple_numb[k])
						# print(i % simple_numb[k])
						simple_numb.append(i)
						#sum_ += simple_numb[arrind]
						# arrind += 1
						break
		for x in simple_numb:
			sum_ += x
		print(simple_numb)
		print( "sum : " + str(sum_))
		return sum_	

if __name__ == "__main__":
	n = PrimeNumbers()
	print(n.SumPrimeNumber(10))