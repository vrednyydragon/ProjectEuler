class Palindrome():
	
	def LargestPalindrome(self, input_data):
		assert 0 < int(input_data), "Вводимые данные должны быть числами больше 0 числами и целыми!!!"
		maxval =int("9"*input_data) 
		minval = int("9"*(input_data-1))
		for i in range(maxval, minval, -1):
		# for i in reversed(range(99,(input_data +1 ),1)):  тоже как вариант можно использовать
			for k in range(maxval, minval, -1):
				result = str(i * k)
				# print (len(str(result))) 
				strlength = len(str(result))
				# strlength = str(result)
				FlagEq = True

				for n in range(0, round(strlength/2), 1):
					# if(FlagEq):
					# 	FlagEq = strlength[n,n+1].......
					#23442

					FlagEq = bool(result[n] == result[strlength-n-1])
					if (not FlagEq):
						break
				if(FlagEq):
					print( str(result) + " - Polindrome");
					return result
		print(-1)
		return -1


if __name__ == "__main__":
	n = Palindrome()
	print(n.LargestPalindrome(3))