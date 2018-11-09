import random
import curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(int(sh), int(sw), 0, 0)
w.keypad(1)
w.timeout(1)

snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]
w.addch(food[0], food[1], "░")

key = curses.KEY_RIGHT
last_key = key
score = 0

while True:
    next_key = w.getch()
    last_key = key if next_key != -1 else last_key
    key = key if next_key == -1 else next_key
    print("")

    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        print("Your score was %s!" % score)
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN and last_key != curses.KEY_UP:
        new_head[0] += 1
    if key == curses.KEY_UP and last_key != curses.KEY_DOWN:
        new_head[0] -= 1
    if key == curses.KEY_LEFT and last_key != curses.KEY_RIGHT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT and last_key != curses.KEY_LEFT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        score += 1
        food = None
        while food is None:
            nf = [
                random.randint(1, int(sh)-1),
                random.randint(1, int(sw)-1)
            ]
            food = nf if nf not in snake else None
        w.addch(int(round(food[0])), int(round(food[1])), "░")
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    try:
        w.addch(int(snake[0][0]), int(snake[0][1]), "▓")
    except:
        curses.endwin()
        print("Your score was %s!" % score)
        quit()
