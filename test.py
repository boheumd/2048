from main import *
from unittest import main, TestCase

# class GameTest has 5 distinct unit test cases | 1(j)(i)
class GameTest(TestCase):
	def test_left(self):
		"test for the direction of left"
		testcases = [ [[2, 0, 2, 4], [2, 2, 2, 2], [4, 8, 0, 16], [8, 16, 4, 0]],
					[[16, 32, 64, 0], [8, 2, 0, 0], [8, 0, 0, 0], [4, 0, 0, 0]] ]
		answers = [ [[4, 4, 0, 0], [4, 4, 0, 0], [4, 8, 16, 0], [8, 16, 4, 0]],
					[[16, 32, 64, 0], [8, 2, 0, 0], [8, 0, 0, 0], [4, 0, 0, 0]] ]

		for i in range(len(testcases)):
			game = newGame(test_field = testcases[i])
			game.move("Left", testmode = True)
			# assertion | 1(j)(ii)
			self.assertEqual(answers[i], game.gameboard.field)
	def test_right(self):
		"test for the direction of right"
		testcases = [ [[2, 0, 2, 4], [2, 2, 2, 2], [4, 8, 0, 16], [8, 16, 4, 0]],
					[[0, 64, 32, 16], [0, 0, 2, 8], [0, 0, 0, 8], [0, 0, 0, 4]] ]
		answers = [ [[0, 0, 4, 4], [0, 0, 4, 4], [0, 4, 8, 16], [0, 8, 16, 4]],
					[[0, 64, 32, 16], [0, 0, 2, 8], [0, 0, 0, 8], [0, 0, 0, 4]] ]

		for i in range(len(testcases)):
			game = newGame(test_field = testcases[i])
			game.move("Right", testmode = True)
			self.assertEqual(answers[i], game.gameboard.field)
	def test_down(self):
		"test for the direction of down"
		testcases = [ [[2, 0, 2, 4], [2, 2, 2, 2], [4, 8, 0, 16], [8, 16, 4, 0]],
					[[0, 0, 0, 0], [0, 0, 0, 0], [4, 2, 0, 0], [32, 8, 4, 0]] ]
		answers = [ [[0, 0, 0, 0], [4, 2, 0, 4], [4, 8, 4, 2], [8, 16, 4, 16]],
					[[0, 0, 0, 0], [0, 0, 0, 0], [4, 2, 0, 0], [32, 8, 4, 0]] ]

		for i in range(len(testcases)):
			game = newGame(test_field = testcases[i])
			game.move("Down", testmode = True)
			self.assertEqual(answers[i], game.gameboard.field)
	
	def test_up(self):
		"test for the direction of up"
		testcases = [ [[2, 0, 2, 4], [2, 2, 2, 2], [4, 8, 0, 16], [8, 16, 4, 0]],
					[[4, 8, 16, 32], [16, 4, 64, 0], [2, 2, 0, 0], [4, 0, 0, 0]] ]
		answers = [ [[4, 2, 4, 4], [4, 8, 4, 2], [8, 16, 0, 16], [0, 0, 0, 0]],
					[[4, 8, 16, 32], [16, 4, 64, 0], [2, 2, 0, 0], [4, 0, 0, 0]] ]

		for i in range(len(testcases)):
			game = newGame(test_field = testcases[i])
			game.move("Up", testmode = True)
			self.assertEqual(answers[i], game.gameboard.field)

	def test_class_board(self):
		"test for the class board"
		# test for add operations
		test_add = [ [[2, 0, 2, 4, 8], [2, 2, 2, 2, 0], [4, 8, 0, 16, 4], [8, 16, 4, 0, 2]],
					[[4, 8, 16, 32], [16, 4, 64, 0], [2, 2, 0, 0], [4, 0, 0, 0]] ]
		temp_board = [ [[2, 0, 2, 4, 8], [2, 2, 2, 2, 0], [4, 8, 0, 16, 4], [8, 16, 4, 0, 2]],
					[[4, 8, 16, 32], [16, 4, 64, 0], [2, 2, 0, 0], [4, 0, 0, 0]] ]
		answer_add = [[[4, 0, 4, 8, 16], [4, 4, 4, 4, 0], [8, 16, 0, 32, 8], [16, 32, 8, 0, 4]],
					[[8, 16, 32, 64], [32, 8, 128, 0], [4, 4, 0, 0], [8, 0, 0, 0]] ]

		for i in range(len(test_add)):
			myboard = board(len(test_add[i]), len(test_add[i][0]), test_add[i])
			myboard = myboard + temp_board[i]
			self.assertEqual(myboard.field, answer_add[i])

		# test for reading or writing an indexed or keyed element
		test_getitem = [ [[2, 0, 2, 4, 8], [2, 2, 2, 2, 0], [4, 8, 0, 16, 4], [8, 16, 4, 0, 2]],
					[[4, 8, 16, 32], [16, 4, 64, 0], [2, 2, 0, 0], [4, 0, 0, 0]] ]
		answer_getitem = [ [2, 0, 2, 4, 8],
					[16, 4, 64, 0] ]
		for i in range(len(test_getitem)):
			myboard = board(len(test_getitem[i]), len(test_getitem[i][0]), test_getitem[i])
			r = myboard[i]
			self.assertEqual(answer_getitem[i], r)
		
		# test the iterable function of the class board
		for i in range(len(test_getitem)):
			myboard = board(len(test_getitem[i]), len(test_getitem[i][0]), test_getitem[i])
			line_number = 0
			for line in myboard:
				self.assertEqual(line, test_getitem[i][line_number])
				line_number += 1

if (__name__ == "__main__"):
	main()
