import logging

# logging.basicConfig(filename="sample.log", level=logging.INFO)
logging.basicConfig(level=logging.INFO)

class Problem059():

	def Pass(self):
		logger = logging.getLogger("Pass")
		logger.info('start')
		self.passwrd = ''
		passwrd = []
		for a in range(97, 123):
			for b in range(97, 123):
				for c in range(97, 123):
					passwrd.append('{}{}{}'.format(chr(a),chr(b),chr(c)))
			# logger.info(str(passwrd))
		# logger.info(str(passwrd))
		return passwrd

	def isletter2(self, a):
		return a <= 122 and a >= 32

	def XOR_Decryption(self, file):
		logger = logging.getLogger("XOR_Decryption")
		logger.info('start')
		new_text = [] # FIXED Add cleaning
		symb = ''
		flag = True
		right_key, encrypted_text = '', ''
		sum_of_scii = 0
		code_txt = open(file, 'r').read().split(",") 
		# logger.info(str(code_txt))
		passwrd = self.Pass()
		xorRez = 0
		for key in passwrd:
			# logger.info('key ' + key)
			for i in range(0, len(code_txt)-2, 3): #здесь я прохожусь циклом через 3 элемента (0, 3, 6 ...)
				new_text = []
				flag = False
				for k in range(3):
					if (k!=0 and not flag):
						break
					xorRez = int(code_txt[i+k])^ord(key[k])
					# logger.info(str(key[k]))
					if (self.isletter2(xorRez)):
						flag = True
					else:
						flag = False
						# logger.info('flag false')
						break
				if not flag:
					# logger.info(chr(xorRez))
					break
			if flag:
				to_return=''
				for i in range(0, len(code_txt)-2, 3):
					for k in range(3):
						to_return += chr(int(code_txt[i+k])^ord(key[k]))
				# logger.info('key ' + key)
				# if ' and ' or ' the ' or ' if ' in to_return:	
				if ' the ' in to_return:
					encrypted_text = to_return
					right_key = key
					logger.info("right key : {}, encrypted text: {} ".format(right_key, encrypted_text))
		for x in encrypted_text:
			sum_of_scii += ord(x)
		return sum_of_scii

if __name__ == "__main__":
	n = Problem059()
	print(n.XOR_Decryption('p059_cipher.txt'))