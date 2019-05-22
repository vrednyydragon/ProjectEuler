# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing
# over five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by
# its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?


class NamesScores():

	def SortingNames(self, input_data):
		names_txt = input_data
		file_names = open(names_txt, 'r')
		print('1')
		names1 = list(file_names)
		#names1 = list(file_names.read().split(','))
		# print(names1.split(','))
		# print(names1)
		# print(names1.split(','))
		# names2 = names1.split(",")
		# # print(names2)
		print('111')
		names2 = str(names1).replace("\"", "")
		# print(names2)
		print(len(names2))
		# print(names2.split(','))
		names2 = ', '.join(sorted(names2.split(',')))
		print(names2)


		# for name in names2:
		# 	print(name)

		#print(file_names.read())
		len_file_names = len(file_names.read())
		# print(len_file_names)

		# print(3)
		# file_names.close()
		# file_names = open(names_txt, 'r')
		# print(file_names.read())

		# # этот метод не работает:
		# print(file_names.readlines())
		# for line in file_names:
		# 	print(line)

		# # это работает
		# with open(names_txt) as file_handler:
		# 	# print(file_names.read())
		# 	print('2')
		# 	for line in file_handler:
		# 		print(line)

		# print(file_names.read())
		file_names.close()


	# file_names1=0
	# with open(names_txt, 'r') as f:
	# 	file_names1 = f.read()
	# 	file_names2 = f.read()
	# 	print(file_names1)
	# 	print(file_names2)
	#


if __name__ == "__main__":
	n = NamesScores()
	## print(n.SortingNames(938))
	print(n.SortingNames('names.txt'))