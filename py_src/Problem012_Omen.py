def triangle_cntdev(in_div_cnt):
	nat_numb = 0
	triangle_numb = 0
	curr_div_cnt = 0
	print ("Ищу нужное число. Подождите плиз ...ё ")
	while in_div_cnt > curr_div_cnt:
		curr_div_cnt = 0
		nat_numb+=1
		triangle_numb+=nat_numb
		#print ("треугольное число: " + str(triangle_numb))
		# это правильный вариант без лимита 500 чисел
		for n in range (1, (triangle_numb+1)):
			if triangle_numb % n == 0:
				curr_div_cnt += 1
				#print ("делитель: " + str(triangle_numb/n))
	else:
		print (" Для искомого колиества делителей : " + str(in_div_cnt))
		print (" Первое подходящее треугольное число: " + str(triangle_numb))

	return (triangle_numb)

triangle_cntdev(6)




