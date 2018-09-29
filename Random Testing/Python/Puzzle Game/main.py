import random as r

#tiles and stuff
w = '▒▒' #wall
b = '  ' #blank
p = '██' #player
dl = '█ ' #door left
dr = ' █' #door right
du = '▀▀' #door up
dd = '▄▄' #door down
f = '░░' #finish
k = '▄▀' #key
s = '--'

#variables
level = 0
a = '\n'*50
message = ''
playerpos = {
	'x':0,
	'y':0
}

#board layouts
board = [
	[
		[w ,w ,w ,w ,w ,w ,w ,w ,w],
		[w ,b ,b ,b ,w ,b ,b ,b ,w],
		[w ,b ,b ,k ,w ,b ,f ,b ,w],
		[w ,b ,b ,b ,w ,b ,b ,b ,w],
		[w ,b ,b ,b ,dl,b ,b ,b ,w],
		[w ,b ,s ,b ,w ,b ,b ,b ,w],
		[w ,b ,b ,b ,w ,b ,b ,b ,w],
		[w ,w ,w ,w ,w ,w ,w ,w ,w]
	]
]

#functions

#check player position or change it
def checkpos():
	global board
	global playerpos
	global p

	board[level][playerpos['y']][playerpos['x']] = p

#print board
def printboard():
	global board
	global level

	checkpos()

	for i in board[level]:
		print(*i, sep='')

#wall
def wall():
	global message

	messages = ['That is a solid walll.','That right there is what humans call a wall, and you cannot in fact phase through it.','Walls are solid.','Stop running into a wall.']
	message = r.choice(messages)

#check for a wall
def checkwall():
	global board
	global level
	global py
	global px
	global w

	if board[level][py-1][px] == w:
		wall()
		return True

	else:
		return(False)

#movement
def move(direction):
	global playerpos
	global px
	global py

	if direction == 'up':
		wall = checkwall()

		if wall:
			return
		else:
			board[level][playerpos['y']][playerpos['x']] = b
			playerpos['y'] -= 1

	if direction == 'down':
		wall = checkwall()

		if wall:
			return
		else:
			board[level][playerpos['y']][playerpos['x']] = b
			playerpos['y'] += 1

	if direction == 'left':
		wall = checkwall()

		if wall:
			return
		else:
			board[level][playerpos['y']][playerpos['x']] = b
			playerpos['x'] -= 1

	if direction == 'right':
		wall = checkwall()

		if wall:
			return
		else:
			board[level][playerpos['y']][playerpos['x']] = b
			playerpos['x'] += 1

#listen for input
def main():
	global inp
	global playerpos
	global board
	global px
	global py
	global message

	px = playerpos['x']
	py = playerpos['y']
	inp = input('')
	message = ''

	movetypes = {
		'w':'up',
		'a':'left',
		's':'down',
		'd':'right'
	}

	inp = movetypes[inp]

	move(inp)

#starting stuff to do
playerpos['y'] = 5
playerpos['x'] = 2

while 1:
	print(a)
	print(message)
	printboard()
	main()
