# print (list(range(999, 98, -1)))
# print (list(reversed(range(99,1000,1))))

# A = [1,2,3,4,5,6]
# B = A[:len(A)/2]
# C = A[len(A)/2:]

# def split_list(a_list):
#	 half = len(a_list)/2
#	 return a_list[:half], a_list[half:]

# A = [1,2,3,4,5,6]
# B, C = split_list(A)


# def split_half(a):
#	 half = len(a) >> 1
#	 return a[:half], a[half:]

# print(split_half([1,2,3,4,5,6])) 


# a = [1,2,3,4,5,6,7,8,9,10]
# print(a[:len(a)/2])
# print(a[len(a)/2:])

# value = 11
# valuе = 32
# print(value)

# def square(x):
# 	"""
# 	Простая функция для вычисления квадрата числа путём сложения.
# 	"""
# 	sum_so_far = 0
# 	for counter in range(x):
# 		sum_so_far = sum_so_far + x
# 		return sum_so_far

# some_dict = {}
# some_dict[5.5] = "Ruby"
# some_dict[5.0] = "JavaScript"
# some_dict[5] = "Python"
# print(some_dict)

# array = [1, 8, 15]
# g = (x for x in array if array.count(x) > 0)
# array = [2, 8, 22]
# print(list(g))

# list_1 = [1, 2, 3, 4]
# list_2 = [1, 2, 3, 4]
# list_3 = [1, 2, 3, 4]
# list_4 = [1, 2, 3, 4]

# for idx, item in enumerate(list_1):
#     del item

# for idx, item in enumerate(list_2):
#     list_2.remove(item)

# for idx, item in enumerate(list_3[:]):
#     list_3.remove(item)

# for idx, item in enumerate(list_4):
#     list_4.pop(idx)
# print(list_1)
# print(list_2)
# print(list_3)
# print(list_4)


# print("\\ some string \\")
# print(r"\ some string")
# print(r"\ some string \")
# a = 256
# b = 256
# print(a is b)

# a = 257
# b = 257
# print(a is b)

# a = 257; b = 257
# print(a is b)

# [] == []
# print([] == [])
# print([] is [])

# a, b = 257, 257
# print(id(a))
# print(id(b))
# print(id(a) == id(b))

# import datetime
# import time

# a = time.ctime(time.time())
# print(a) # Wed Apr 5 00:13:47 2017

# # x = time.time()
# # print(x) # 1491340367.478385

# date = datetime.datetime.today()
# print('now ', date)
# for yy in range (2005, 2010):
# 	for mm in range (1, 13):
# 		d = datetime.datetime(yy, mm, 1).isoweekday()
# 		print(d)

# from datetime import date
# import calendar

# my_date = date.today()

# print(calendar.day_name[my_date.weekday()])

# # print(calendar.day_name[6])
# print(my_date.weekday())

str = "this is my line....wow!!!"
print (str.split( ))
print (str.split('i',1))
print (str.split('w'))

