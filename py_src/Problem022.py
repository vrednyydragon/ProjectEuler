# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing
# over five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by
# its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?


class NamesScores():

	def SortingNames(self, input_data1, input_data2):
		names_txt = input_data1
		numb_name_for_test = input_data2
		sum_letter_name = 0
		sum_of_names = 0
		file_names = open(names_txt, 'r')
		# print('1')
		names1 = file_names.read().replace("\"", "") #str()
		# print(names1)
		#list_names = ' '.join(sorted(names1.split(','))).split()
		list_names = sorted(names1.split(','))
		print(list_names)
		len_list_names = len(list_names)
		print(len_list_names)
		print('Tестовое имя по номеру ' + str(numb_name_for_test)+ ": "
		      + str(list_names[numb_name_for_test-1]))
		for i in range(len_list_names):
			# print("Порядковый номер имени: " + str(i+1) + ". Имя: " + str(list_names[i])
			#       + '. Длина имени: ' + str(len(list_names[i])))
			print(str(i+1) + ' - ' + str(list_names[i]))
			sum_letter_name = 0
			for k in list_names[i]:
				# print(str(k) + ' - ' + str(ord(k)-64))
				# # по ASCII A - 65, нужно отнять -64 чтобы получить А - 1
				sum_letter_name += ord(k) - 64
			print('Сумма букв имени - ' + str(sum_letter_name))
			print(sum_letter_name * (i+1))
			sum_of_names += (sum_letter_name * (i+1))
			# # для теста, это правильно выводится но... нужно отдельно это сделать для теста
			# # возможно функцией
			# if i+1 == numb_name_for_test:
			# 	print(str(i+1) + ' - ' + str(list_names[i]) + ' сумма имени - ' +
			# 	      str(sum_letter_name) + ", сумма имени умноженая на номер -" +
			# 	      str(sum_letter_name * (i+1)))
		print("Сумма всех имен в файле - " + str(sum_of_names))
		file_names.close()
		return sum_of_names

if __name__ == "__main__":
	n = NamesScores()
	## print(n.SortingNames(938))
	print(n.SortingNames('names.txt', 938))