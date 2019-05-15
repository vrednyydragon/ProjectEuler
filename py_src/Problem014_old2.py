#The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
class Sequence():

	# в этой функции, используя входящий параметр, мы генерируем одну последовательность:
	def GeneratingOfSequence(self, input_data):
		# сразу проверяем условие что входящий параметр число и тд... 
		# и если условие ложно, немедленно вызвать ошибку с описанием что не так
		assert 0 < int(input_data), "Вводимые данные должны быть числами больше 0 числами и целыми!!!"
		# приводим входящие даные в число
		n = int(input_data)
		i = 0
		# print('Последовательность чисел начинается с натурального числа :' + str(n))
		# пока переменная не будет равняться 1, условие будет выполняться
		while n != 1:
			if n%2 == 0:
				n = n/2
				# print(n)
			else :
				n = 3*n + 1
				# print (n)
			i += 1	
			# print('количество итераций ' + str(i+1))	
		# print('количество итераций ' + str(i))
		# print('эта последовательность начиная с ' + str(input_data) + ' и заканчивая ' + str(n) + ' содержит ' + str(i+1) + ' членов.')
		# print (n)
		return i+1
	#  в этой функции перебираем числа, находим максимальную цепочку последовательности
	# и выводим число с которого она начинается
	def MaxSequence(self, input_data):
		numb_list = []
		n = int(input_data)
		for i in range (2, n+1):
			# это плохое решение 
			# print(Sequence.GeneratingOfSequence(i)) 
			numb_list.append(self.GeneratingOfSequence(i))
		return max(numb_list) 	

		
if __name__ == "__main__":
    # print(Sequence.GeneratingOfSequence(13))
		n = Sequence()
		print(n.MaxSequence(13))