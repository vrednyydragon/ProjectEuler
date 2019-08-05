# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral 
# is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

import logging
# logging.basicConfig(filename="sample.log", level=logging.INFO)
logging.basicConfig(level=logging.INFO)

class Problem028(object):
	"""docstring for Problem028"""
	def __init__(self, arg=0):
		super(Problem028, self).__init__()
		self.sideLen = arg
		self.Matrix = [[0 for x in range(arg)] for y in range(arg)]
		for row in self.Matrix: 
			logging.info(str(row))

	def changeStepDirrectoin(self, x, y, dir):
		logging.info('start changeStepDirrectoin x{} y{} dir{}'.format(x,y,dir))
		if dir == 0: # вправо
			x, y = x, y+1
		if dir == 1: # вниз
			x, y = x+1, y
		if dir == 2: # влево
			x, y = x, y-1
		if dir == 3: # вверх
			x, y = x-1, y
		logging.info('return x{} y{} dir{}'.format(x,y,dir))
		return x, y

	def fillMatrixSpiral(self):
		logging.info('start fillMatrixSpiral')
		i = 1
		x = int(self.sideLen/2)
		y = int(self.sideLen/2)
		self.Matrix[x][y] = i
		stepLen = 1
		stepDirection = 1 # вправо влево вверх вниз
		logging.debug('x <{}> y <{}> i <{}>'.format(x, y, i))
		# loop for directions
		while i < self.sideLen*self.sideLen and x < self.sideLen and y < self.sideLen and x>=0 and y >=0:
			for d in (range(4)):
				#print('d <{}>'.format(d))
				# loop for stepLen
				for s in (range(stepLen)):
					#print('s <{}> d <{}>'.format(s,d))
					x,y = self.changeStepDirrectoin(x,y,d)
					if x < self.sideLen and y < self.sideLen and x>=0 and y >=0:
						i += 1
						self.Matrix[x][y] = i
				if d in [1,3]:
					stepLen +=1

		self.printMatrix(1)
		logging.info('finish fillMatrixSpiral')

	def fillMatrixLiner(self):
		logging.info('start fillMatrixLiner')
		logging.info('finish fillMatrixLiner')

	def printMatrix(self, printtype = 0):
		logging.info('start printMatrix printtype {}'.format(printtype))
		if (printtype == 0):
			for row in self.Matrix: 
				logging.info(str(row))
		if (printtype == 1): # straight christ
			christPosition = int(self.sideLen/2)
			logging.info('christPosition {}'.format(christPosition))
			for x in (range(self.sideLen)):
				row2Print = ""
				for y in (range(self.sideLen)):
					rowformat = "  {}  "
					if x == christPosition or y == christPosition:
						rowformat = ' ({}) '
					#row2Print += '<{},{}>'.format(x,y) + rowformat.format(self.Matrix[x][y])
					row2Print += rowformat.format(self.Matrix[x][y])
				logging.info(row2Print)
		if (printtype == 2): # x christ
			for x in (range(self.sideLen)):
				row2Print = ""
				for y in (range(self.sideLen)):
					rowformat = "  {}  "
					if x==y or x+y == self.sideLen-1:#x == christPosition or y == christPosition:
						rowformat = ' ({}) '
					#row2Print += '<{},{}>'.format(x,y) + rowformat.format(self.Matrix[x][y])
					row2Print += rowformat.format(self.Matrix[x][y])
				logging.info(row2Print)
		if (printtype == 3): # coords
			for x in (range(self.sideLen)):
				row2Print = ""
				for y in (range(self.sideLen)):
					row2Print += ' ({},{} <{}>) '.format(x,y,self.Matrix[x][y])
				logging.info(row2Print)

if __name__ == "__main__":
	# n = SpiralArr()
	# print(n.FindDiagonalSum(5, 5))
	k = Problem028(6)
	k.fillMatrixSpiral()