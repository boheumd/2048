# This is a custom module | 1(h)
# And this is a custom module that can also be used as a scipt | 2(g)
from logging import root, debug, info, warning, error, critical
from logging import root
import os

# decorator() is a custom function | 1(f)(i)
# decorator() is a function that outputs a function | 1(f)(vii)
# decorator() is a decorator function | 2(n)
def decorator(func):
	step = 0
	# wrapped() is a function that takes unlimited parameters | 2(i)
	def wrapped(*ordered, **unordered):
		# inner function using nonlocal scope | 2(j)
		nonlocal step
		step += 1
		os.system("clear")
		# str(step) str object | 1(d)(ii)
		print("current_steps: " + str(step))
		return func(*ordered, **unordered)
	return wrapped



@decorator
def display(height = 4, width = 4):
	# local variable separate_line | 1(a)(ii)
	separate_line = "-" * (6 * width + 1)
	def draw(field):
		for row in range(height):
			print(separate_line)
			# map function | 1(b)(ii)
			l = map(lambda v: "%5d" %v, field[row])
			print("|" + "|".join(l) + "|")
		print(separate_line)
	return draw

def transpose(field):
	return [list(row) for row in zip(*field)]

def invert(field):
	return [row[::-1] for row in field]

def write_logs():
	debug("Things happening behind the scenes, that might be useful.")
	info("Information about the progress of the program.")
	warning("This is not good, but let the user decide.")
	error("Something that should not happen happened.")
	critical("Like an error, but also not recoverable.")

def reset_settings():
	for handler in root.handlers:
		root.removeHandler(handler)

if __name__ == "__main__":
	f = [[1028 for i in range(5)] for j in range(5)] 
	print(f)
	draw_field = display(5, 5)
	draw_field(f)