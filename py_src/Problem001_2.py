
class Sum():
	
	def SumMultiplues(self, input_data):
		assert 0 < int(input_data), "Вводимые данные должны быть числами больше 0 числами и целыми!!!"
		numb = int(input_data)
		iterator=0 
		sum_ = 0
		for i in range (numb):
			iterator=i
			if (iterator%3==0 or iterator%5==0):
				print("кратное 3 или 5: " + str(iterator))
				sum_+=iterator
		print("сумма чисел кратных 3 и 5 : " + str(sum_))
		return sum_

if __name__ == "__main__":
	n = Sum()
	print(n.SumMultiplues(1000))








'''iterator=0 
sum_ = 0 

for i in range (1000):
	iterator=i
	if (iterator%3==0 or iterator%5==0):
		print("кратное 3 или 5: " + str(iterator))
		sum_+=iterator 
	


print("сумма чисел кратных 3 и 5 : " + str(sum_))'''
