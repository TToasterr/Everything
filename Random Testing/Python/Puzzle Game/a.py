import random as r

#tiles
w = '▒▒' #wall
b = '  ' #blank
p = '██' #player
dl = '█ ' #door left
dr = ' █' #door right
du = '▀▀' #door up
dd = '▄▄' #door down
f = '░░' #finish
k = '▄▀' #key
pi = '↑↑' #portal in
po = '↓↓' #portal out
ui = '←←' #portal 2 in
uo = '→→' #portal 2 out
s = '--' #start

#variables
level = 0
a = '\n'*50
message = ''
px = 2
py = 5
key = 0

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
	],
    [
		[w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w],
		[w ,b ,b ,b ,w ,b ,b ,b ,b ,b ,w ,w ,b ,b ,b ,b ,b ,w],
		[w ,b ,s ,b ,w ,b ,b ,b ,k ,b ,w ,w ,b ,b ,b ,b ,k ,w],
		[w ,b ,b ,b ,w ,b ,b ,b ,b ,b ,b ,w ,b ,b ,b ,b ,b ,w],
		[w ,b ,b ,b ,dl,b ,b ,b ,b ,b ,b ,dl,b ,b ,b ,b ,b ,w],
		[w ,b ,b ,b ,w ,b ,b ,b ,b ,b ,b ,w ,b ,b ,b ,b ,b ,w],
		[w ,b ,b ,b ,w ,b ,b ,b ,b ,b ,b ,w ,b ,k ,b ,b ,b ,w],
		[w ,b ,k ,b ,w ,b ,b ,b ,b ,b ,b ,w ,b ,b ,b ,b ,b ,w],
		[w ,b ,b ,b ,w ,b ,b ,b ,b ,b ,b ,w ,w ,w ,du,w ,w ,w],
		[w ,b ,b ,b ,w ,b ,b ,b ,b ,b ,b ,w ,w ,w ,du,w ,w ,w],
		[w ,b ,b ,w ,w ,b ,b ,b ,b ,b ,b ,w ,w ,b ,b ,b ,b ,w],
		[w ,b ,b ,w ,w ,b ,b ,b ,b ,b ,b ,w ,w ,b ,b ,f ,b ,w],
		[w ,b ,b ,w ,w ,b ,b ,b ,b ,b ,b ,w ,w ,b ,b ,b ,b ,w],
		[w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w]
    ],
    [
		[w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w],
		[w ,s ,b ,w ,w ,w ,w ,b ,b ,b ,w ,b ,b ,b ,b ,b ,b ,w],
		[w ,b ,b ,w ,w ,w ,w ,b ,f ,b ,w ,b ,b ,k ,b ,b ,b ,w],
		[w ,b ,b ,w ,w ,w ,w ,b ,b ,b ,w ,b ,b ,b ,b ,b ,b ,w],
		[w ,b ,b ,w ,w ,w ,w ,b ,uo,b ,w ,b ,b ,b ,b ,b ,b ,w],
		[w ,b ,b ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,dd,w ,w ,du,w],
		[w ,b ,b ,w ,w ,w ,w ,b ,b ,b ,b ,b ,b ,b ,w ,b ,b ,w],
		[w ,b ,b ,w ,w ,w ,w ,b ,po,b ,b ,k ,b ,b ,w ,b ,b ,w],
		[w ,b ,b ,w ,w ,w ,w ,b ,b ,b ,w ,w ,w ,w ,w ,k ,b ,w],
		[w ,b ,b ,w ,w ,w ,w ,w ,w ,w ,w ,b ,b ,b ,dr,b ,b ,w],
		[w ,b ,b ,b ,w ,w ,w ,b ,b ,b ,b ,b ,b ,w ,w ,w ,w ,w],
		[w ,b ,k ,b ,w ,w ,w ,w ,b ,b ,k ,b ,b ,w ,b ,b ,b ,w],
		[w ,b ,b ,b ,w ,b ,pi,w ,w ,b ,b ,b ,b ,dl,b ,ui,b ,w],
		[w ,b ,b ,b ,dl,b ,b ,w ,w ,w ,w ,b ,b ,w ,b ,b ,b ,w],
    	[w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w ,w],
    ]
]



#functions

#print the board
def printboard():
    global board, level

    for i in board[level]:
        print(*i, sep='')



#movement
def move(coord):
    global message, board, level, px, py, key

    board[level][py][px] = b
    pyt = coord[0]
    pxt = coord[1]

    if board[level][pyt][pxt] == f:
        level += 1
        for i in range(len(board[level])):
            for a in range(len(board[level][i])):
                if board[level][i][a] == s:
                    py = i
                    px = a
        return

    elif board[level][pyt][pxt] == pi:
        for i in range(len(board[level])):
            for a in range(len(board[level][i])):
                if board[level][i][a] == po:
                    py = i - 1
                    px = a
        return

    elif board[level][pyt][pxt] == ui:
        for i in range(len(board[level])):
            for a in range(len(board[level][i])):
                if board[level][i][a] == uo:
                    py = i - 1
                    px = a
        return

    elif board[level][pyt][pxt] == w:
        message = 'Thats a reliatively solid wall.'
        return

    elif board[level][pyt][pxt] == po or board[level][pyt][pxt] == uo:
        message = 'You cant go back through a portal.'
        return

    elif board[level][pyt][pxt] == k:
        message = 'You got a key!'
        key += 1

    elif board[level][pyt][pxt] == dl or board[level][pyt][pxt] == dr or board[level][pyt][pxt] == du or board[level][pyt][pxt] == dd:
        if key >= 1:
            message = 'You opened the door!'
            key -= 1

        else:
            message = 'You dont have a key!'
            return

    py = pyt
    px = pxt



#listening for input
def main():
    global inp, message, px, py
    inp = input()
    message = ''

    stuff = {
        'w':[py - 1, px],
        'a':[py, px - 1],
        's':[py + 1, px],
        'd':[py, px + 1]
    }

    try:
        m = stuff[inp]
        move(m)
    except:
        message = 'That isnt a command.'



#starting stuff
while 1:
    try:
        board[level][py][px] = p
    except:
        message = 'This level isnt done yet!'
    print(a)
    print(message)
    print('py: %s\npx: %s' % (py, px))
    printboard()
    main()
