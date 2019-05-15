class Grid():
	def MultiplyAdjacentNumbers(self, in_numbers):
		assert 0 < int(in_numbers), "Вводимые данные должны быть числами больше 0 числами и целыми!!!"
		list1=["08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08",
		       "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00",
		       "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65",
		       "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91",
		       "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80",
		       "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50",
		       "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70",
		       "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21",
		       "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72",
		       "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95",
		       "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92",
		       "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57",
		       "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58",
		       "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40",
		       "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66",
		       "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69",
		       "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36",
		       "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16",
		       "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54",
		       "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"]
		L = len(list1)
		N = int(in_numbers)
		ML = L - N + 1 #(17)
		mult = 1
		max_mult = 0
		max_x = 0
		max_y = 0
		max_D = 0
		numb_list = []


		for i in range(L):
			list1[i] = [int(m) for m in list1[i].split(' ')]

		for y in range (L):
			for x in  range(L):
				# блок расчета по вернтикали
				if (x < ML):
					mult = 1
					for n in range(N):
						# print(x, y, list1[x+n][y] )
						mult *= list1[x+n][y]
					# print(mult)
					if mult > max_mult:
						max_mult = mult
						max_x = x
						max_y = y
						max_D = 'horizontal'
						# print(max_mult)
				# блок расчета по горизонтали
				if (y < ML):
					mult = 1
					for n in range(N):
						# print(x, y, list1[x][y+n])
						mult *= list1[x][y + n]
					if mult > max_mult:
						max_mult = mult
						max_x = x
						max_y = y
						max_D = 'vertical'
						# print(max_mult)
				#блок расчета по диагонали 0 ----> ML
				if (x < ML) and (y < ML):
					mult = 1
					for n in range(N):
						# print(x, y, list1[x+n][y+n])
						mult *= list1[x+n][y+n]
						# print(mult)
					if mult > max_mult:
						max_mult = mult
						max_x = x
						max_y = y
						max_D = 'R-diagonal'
					# print(max_mult)
				#блок расчета по диагонали  N ----> L
				if (x > N-2) and (y < ML):
					mult = 1
					for n in range(N):
						# print(x, y, list1[x-n][y+n])
						mult *= list1[x-n][y+n]
						# print(mult)
					if mult > max_mult:
						max_mult = mult
						max_x = x
						max_y = y
						max_D = 'L-diagonal'

		print('направление умножаемых чисел: ' + max_D)
		if max_D == 'horizontal':
			for n in range(N):
				# print(list1[max_x+n][max_y])
				numb_list.append(list1[max_x+n][max_y])
		if max_D == 'vertical':
			for n in range(N):
				# print(list1[max_x][max_y+n])
				numb_list.append(list1[max_x][max_y+n])
		if max_D == 'R-diagonal':
			for n in range(N):
				# print(list1[max_x+n][max_y+n])
				numb_list.append(list1[max_x+n][max_y+n])
		if max_D == 'L-diagonal':
			for n in range(N):
				# print(list1[max_x-n][max_y+n])
				numb_list.append(list1[max_x-n][max_y+n])
			for i in range(L):
				print(list1[i])
		print('координаты по горизонтали х = ' + str(max_x) + ', по вертикали y = ' + str(max_y))
		print('направление умножаемых чисел: ' + str(max_D))
		print('множители: ' + str(numb_list) + 'сумма этих множителей: ' + str(max_mult))


		return numb_list, max_mult

if __name__ == "__main__":
	n = Grid()
	print(n.MultiplyAdjacentNumbers(6))

