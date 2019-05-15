class PrimeFactors():
	
	def PrimeFactorsMaxNumber(self, input_data):
		assert 0 < int(input_data), "Вводимые данные должны быть числами больше 0 числами и целыми!!!"
		numb = int(input_data)
		print("start")
		simple_numb = [2]
		# simple_numb[0] = 2
		arrind=0
		for i in range (numb):
			# print("iteration: " +str(i))
			if ((i>0) and (i%2>0)):
				k = 0
				while k <= arrind:
					if((i % simple_numb[k] == 0) or (i <= simple_numb[k])):
						# print("((i simple_numb[k] == 0) or (i <= simple_numb[k]))")
						break
					if(k == arrind):
						# print("if(k == arrind)")
						arrind += 1 
						simple_numb.append(i)
						# print("get simple numb "+str(i))
						break
					k+=1
		# print("simple_numb filled")
		del_ = input_data
		# print("del_  " + str(del_))
		for_return = []
		while(True):
			for i in range (arrind):
				if( del_ % simple_numb[i] == 0):
					del_ = del_ / simple_numb[i]
					print("simple_numb " +str(simple_numb[i])  + " del_ " + str(del_))
					for_return.append(simple_numb[i])
					break
			if (del_ == 1):
				break
		#print(for_return)
		return max(for_return)

if __name__ == "__main__":
	n = PrimeFactors()
	print(n.PrimeFactorsMaxNumber(13195))
	# PrimeFactors.PrimeFactorsMaxNumber(13195)