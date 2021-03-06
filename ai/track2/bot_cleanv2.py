#!/usr/bin/python

import random

# Head ends here
def next_move(posx, posy, board):
    """
    Description of the algorithm:
        Find out the nearest dirty cell among all the dirty cells and then determine the next move, if no dirty cell found, select a stochastic direction according the invisible cells
    """
    all_positions = [(x, y) for x in xrange(0, 5) for y in xrange(0, 5)]
    dirty_cells = []
    invisible_cells = []
    for (x, y) in all_positions:
        if board[x][y] is 'd':
            dirty_cells.append((x, y))
        if board[x][y] is 'o':
            invisible_cells.append((x, y))
    nearest_dirty_cell = ()
    nearest_dirty_steps = 8
    for (x, y) in dirty_cells:
        steps = abs(x - posx) + abs(y - posy)
        if nearest_dirty_cell is ():
            nearest_dirty_cell = (x, y)
            nearest_dirty_steps = steps
        if steps < nearest_dirty_steps:
            nearest_dirty_cell = (x, y)
            nearest_dirty_steps = steps
    random_invisible_cell = invisible_cells[random.randint(0, len(invisible_cells) - 1)]
    result = ""
    if nearest_dirty_cell is ():
        if posy < random_invisible_cell[1]:
            result = "RIGHT"
        elif posy > random_invisible_cell[1]:
            result = "LEFT"
        elif posx < random_invisible_cell[0]:
            result = "DOWN"
        elif posx > random_invisible_cell[0]:
            result = "UP"
    elif nearest_dirty_steps is 0:
        result = "CLEAN"
    elif posy < nearest_dirty_cell[1]:
        result = "RIGHT"
    elif posy > nearest_dirty_cell[1]:
        result = "LEFT"
    elif posx < nearest_dirty_cell[0]:
        result = "DOWN"
    elif posx > nearest_dirty_cell[0]:
        result = "UP"
    print result

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
