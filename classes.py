from random import randint, choice
from json import load, dump
from functions import *

# class board is a custom class | 1(g)(i)
# class board is an iterable class | 1(g)(iii)
# class board has private field "__current_index" | 1(g)(iv)
# class board has public field "height" | 1(g)(v)
# class board supports "+" operation | 1(g)(vi)
# class board supports reading or writing an 
# indexed or keyed element | 1(g)(vii)
class board:
	height = None
	width = None
	field = None
	__current_index = None
	def __init__(self, height = 4, width = 4, data = []):
		self.height = height
		self.width = width
		# if and else | 1(e)(i) 
		if(data == []):
			# in operation | 1(c)(i)
			# list comprehension | 1(c)(ii)
			# list object | 1(d)(i)
			# range object | 1(d)(iii)
			self.field = [[0 for i in range(self.width)] for j in range(self.height)] 
		else:
			self.field = data

	def __add__(self, tempBoard):
		# for loop | 1(e)(ii)
		for i in range(self.height):
			for j in range(self.width):
				self[i][j] += tempBoard[i][j]
		return self
	def __radd__(self, tempBoard):
		for i in range(self.height):
			for j in range(self.width):
				self[i][j] += tempBoard[i][j]
		return self

	def __getitem__(self, k):
		"""return a list representing the kth row"""
		if(k < self.height):
			return self.field[k]

	def __setitem__(self, k, v):
		"""set the kth row to v, v must be a list"""
		# len function | 1(b)(i)
		if(k < self.height and len(v) == self.width):
			self.field[k] = v

	def __iter__(self):
		self.__current_index = 0
		return self

	def __next__(self):
		if self.__current_index >= self.height:
			raise StopIteration
		else:
			self.__current_index += 1
			return self[self.__current_index-1]




class Game:
	"""docstring for Game"""
	height = None
	width = None
	score = None
	target = None
	highest = None
	gameboard = None
	lastfield = None
	lastscore = None

	def __init__(self, test_field = []):
		"""read height, width, score, target, field from the file"""
		
		# try and except that specifies the Exception type | 1(e)(iv)
		try:
			# reading from json file save.json | 1(i)(iii)
			# a with block | 2(h)
			# processing input from JSON | 2(k)
			with open("save.json", "r") as ipf:
				loaded = load(ipf)
				self.height = loaded["height"]
				self.width = loaded["width"]
				self.score = loaded["score"]
				self.highest = loaded["highest"]
				self.target = loaded["target"]
				data = loaded["field"]
				self.gameboard = board(self.height, self.width, data)
		except FileNotFoundError:
			print("File not found, please start a new game")
			exit(-1)

	def __move_is_possible(self, direction):
		def move_left_is_possible(field):
			flag = False
			for row in field:
				for i in range(len(row)-1):
					if(row[i] == 0 and row[i+1] != 0):
						return True
					if(row[i] == row[i+1] and row[i] != 0):
						return True
			return False

		move_possible = {}
		# functions defined using lambda | 1(f)(iv)
		move_possible["Left"] = lambda field: move_left_is_possible(field)
		move_possible["Right"] = lambda field: move_possible["Left"](invert(field))
		move_possible["Up"] = lambda field: move_possible["Left"](transpose(field))
		move_possible["Down"] = lambda field: move_possible["Right"](transpose(field))

		if direction in move_possible.keys():
			return move_possible[direction](self.gameboard.field)
		else:
			return False

	# a function with optional arguments | 1(f)(ii)
	def move(self, direction, testmode = False):
		"""move in the direction and update the field"""
		def move_row_left(row):
			# A function that changes one of its arguments
			# tighten function changes its argument "row" | 1(f)(v)
			def tighten(row):
				length = len(row)
				new_row = [t for t in row if t != 0]
				row = new_row + [0 for i in range(length - len(new_row))]
				return row

			def combine(row):
				new_row = []
				i = 0
				# while loop | 1(e)(iii)
				while(i < len(row)):
					if(i+1 < len(row) and row[i] == row[i+1]):
						new_row.append(row[i]*2)
						self.score += 2 * row[i]
						i = i + 2
					else:
						new_row.append(row[i])
						i = i + 1
				new_row += [0 for i in range(len(row) - len(new_row))]
				assert(len(new_row) == len(row))
				return new_row
			return combine(tighten(row))

		move_rows = {}
		move_rows["Left"] = lambda field : [move_row_left(row) for row in field]
		move_rows["Right"] = lambda field : invert(move_rows["Left"](invert(field)))
		move_rows["Up"] = lambda field : transpose(move_rows["Left"](transpose(field)))
		move_rows["Down"] = lambda field : transpose(move_rows["Right"](transpose(field)))
		
		if direction in move_rows.keys():
			if self.__move_is_possible(direction):
				self.lastfield = self.gameboard.field
				self.lastscore = self.score
				self.gameboard.field = move_rows[direction](self.gameboard.field)
				if(testmode == False):
					self.spawn()
				temp = []
				for row in self.gameboard:
					temp += row
				self.highest = max(temp)
				return True
			else:
				return False


	def is_win(self):
		"""if win or not"""
		if(self.highest >= self.target):
			return True
		else:
			return False

	def is_lose(self):
		"""if win or not"""
		def full_of_tiles():
			for row in self.gameboard:
				for e in row:
					if(e == 0):
						return False
			return True
		if(full_of_tiles() and not any(self.__move_is_possible(direction) for direction in ["Left", "Right", "Up", "Down"]) ):
			return True
		else:
			return False

	def spawn(self):
		"""produce new tile with value 2 or 4"""
		z = randint(0, 2)
		(x, y) = choice([(x, y) for x in range(self.height) for y in range(self.width) if self.gameboard[x][y] == 0])
		if(z % 2 == 0):
			tempLine = [0 if i != y else 2 for i in range(self.width)]
			tempBoard = [[0 for j in range(self.height)] if i != x else tempLine for i in range(self.height)]
		else:
			tempLine = [0 if i != y else 4 for i in range(self.width)]
			tempBoard = [[0 for j in range(self.height)] if i != x else tempLine for i in range(self.height)]
		self.gameboard = self.gameboard + tempBoard

	def undo(self):
		if(self.lastfield != None and self.lastscore != None):
			self.gameboard.field = self.lastfield
			self.score = self.lastscore
			self.lastfield = None
			self.lastscore = None
		else:
			print("Sorry, you can undo for just one step")

	def save(self):
		TO_SAVE = {}
		TO_SAVE["height"] = self.height
		TO_SAVE["width"] = self.width
		TO_SAVE["score"] = self.score
		TO_SAVE["target"] = self.target
		TO_SAVE["highest"] = self.highest
		TO_SAVE["field"] = self.gameboard.field
		# writing to a save.json file | 1(i)(iv)
		with open("save.json", "w") as opf:
			dump(TO_SAVE, opf)

# class newGame is a subclass of class Game | 1(g)(ii)
class newGame(Game):
	def __init__(self, height = 4, width = 4, target = 2048, test_field = []):
		"""start a new game"""
		if test_field != []:
			self.height = len(test_field)
			self.width = len(test_field[0])
			self.gameboard = board(self.height, self.width, test_field)
			self.score = 0
			self.target = target
			self.highest = 0
		else:
			try:
				temp = input("Please input the height of the board(default value = 4): ")
				if(len(temp) > 0):
					height = int(temp)
				temp = input("Please input the width of the board(default value = 4): ")
				if(len(temp) > 0):
					width = int(temp)		
				temp = input("Please input the target value of this game(default value = 2048): ")
				if(len(temp) > 0):
					target = int(temp)	
			except:
				print("Invalid input value")
				exit(-1)
			self.height = height
			self.width = width
			self.score = 0
			self.target = target
			self.highest = 0
			self.gameboard = board(height, width)
			self.spawn()
			self.spawn()