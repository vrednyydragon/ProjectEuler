class SumInTriangle():

	def MaximumPathSum(self, input_data):

		trianglestr = input_data
		# trianglestr = ["3",
		# 			"7 4",
		# 			"2 4 6",
		# 			"8 5 9 3"]
		# trianglestr = ["75",
		# 				"95 64",
		# 				"17 47 82",
		# 				"18 35 87 10"]
		# trianglestr = ["75",
		# 				"95 64",
		# 				"17 47 82",
		# 				"18 35 87 10",
		# 				"20 04 82 47 65",
		# 				"19 01 23 75 03 34",
		# 				"88 02 77 73 07 63 67",
		# 				"99 65 04 28 06 16 70 92",
		# 				"41 41 26 56 83 40 80 70 33",
		# 				"41 48 72 33 47 32 37 16 94 29",
		# 				"53 71 44 65 25 43 91 52 97 51 14",
		# 				"70 11 33 28 77 73 17 78 39 68 17 57",
		# 				"91 71 52 38 17 14 91 43 58 50 27 29 48",
		# 				"63 66 04 68 89 53 67 30 73 16 69 87 40 31",
		# 				"04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"]
		lenght = len(trianglestr)
		triangle_basic=[None for m in range(lenght)]
		triangle=[None for m in range(lenght)]

		# print(triangle_basic)
		# print(lenght)
		for i in range(lenght):
			triangle[i] = [int(m) for m in trianglestr[i].split(' ')]
			triangle_basic[i] = [int(m) for m in trianglestr[i].split(' ')]

		# print(triangle.__len__())
		## кусок задачи, где ссумирование чисел идет снизу вверх к вершине
		# x = lenght-2
		# print(triangle)
		# while x >= 0:
		# 	print("x " + str(x))
		# 	for y in range(len(triangle[x])):
		# 		#print(triangle[x][y])
		# 		triangle[x][y] += max(triangle[x+1][y], triangle[x+1][y+1])
		# 	#print(triangle[x][y])
		# 	x -= 1

		# суммирование чисел идет сверху вниз к основанию треугольника
		for x in range(1, lenght):
			# print("x " + str(x))
			for y in range(len(triangle[x])):
				if y == 0:
					triangle[x][y] += triangle[x-1][y]
				elif y == len(triangle[x-1]):
					triangle[x][y] += triangle[x-1][y-1]
				else:
					triangle[x][y] += max(triangle[x - 1][y-1], triangle[x - 1][y])
		# print(triangle)
		for i in range(len(triangle)):
			# print(triangle[i].index(max(triangle[i])))
			str2output =""
			for k in range(len(triangle[i])):
				if (k == triangle[i].index(max(triangle[i]))):
					str2output += "[" + str(triangle_basic[i][k]) + "] "
				else:
					str2output += str(triangle_basic[i][k]) + " "
			print(str2output)
		for i in range(len(triangle)):
			print(triangle[i])
		return max(triangle[i])

if __name__ == "__main__":
    n = SumInTriangle()
    a = ["3",
		"7 4",
		"2 4 6",
		"8 5 9 3"]
    print(n.MaximumPathSum(a))




