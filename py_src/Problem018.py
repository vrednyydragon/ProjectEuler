triangle = ["3",
			"7 4",
			"2 4 6",
			"8 5 9 3"]
sum1 = 0
T1 = [[], [], [], [], [], [], [], []]

lenght = len(triangle)
print(lenght)
for i in range(lenght):
	triangle[i] = [int(m) for m in triangle[i].split(' ')]


print(triangle.__len__())
x = lenght-2
# print(triangle)
while x >=0:
	print("x " + str(x))
	for y in range(len(triangle[x])):
		#print(triangle[x][y])
		triangle[x][y] += max(triangle[x+1][y], triangle[x+1][y+1])
		#print(triangle[x][y])
	x-=1
		# triangle[x][y] += triangle[x + 1][y + 1]
print(triangle)





