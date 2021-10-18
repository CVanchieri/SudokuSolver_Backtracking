import pprint
import numpy as np
import pprint

### Create a random Sudoku Bard ###
base  = 3
side  = base*base

# pattern for a baseline valid solution
def pattern(r,c): return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)
from random import sample
def shuffle(s): return sample(s,len(s)) 
rBase = range(base) 
rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
nums  = shuffle(range(1,base*base+1))

# create a full board using randomized baseline pattern
board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
full_board = []
for line in board: 
    # print(line)
    full_board.append(line)
pp = pprint.PrettyPrinter(width=41, compact=True)
print('--Random Sudoku Board--')
pp.pprint(full_board)
# create board with missing numbers 
squares = side*side
empties = squares * 3//4
for p in sample(range(squares),empties):
    board[p//side][p%side] = 0

numSize = len(str(side))
config_board = []
for line in board: 
    # print("["+" , ".join(f"{n or 0:{numSize}}" for n in line)+"],")
    config_board.append(line)
pp = pprint.PrettyPrinter(width=41, compact=True)
print('--Created Sudoku Board--')
pp.pprint(config_board)

### solve the given Sudoku board ###
def solve(bo):
    """
    Solves a sudoku board using backtracking
    :param bo: 2d list of ints
    :return: solution
    """
    find = find_empty(bo)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if valid(bo, (row, col), i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def valid(bo, pos, num):
    """
    Returns if the attempted move is valid
    :param bo: 2d list of ints
    :param pos: (row, col)
    :param num: int
    :return: bool
    """
    # Check row
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Col
    for i in range(0, len(bo)):
        if bo[i][pos[1]] == num and pos[1] != i:
            return False

    # Check box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def find_empty(bo):
    """
    finds an empty space in the board
    :param bo: partially complete board
    :return: (int, int) row col
    """
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None


def print_board(bo):
    """
    prints the board
    :param bo: 2d List of ints
    :return: None
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")

### manually create a board ###
# board = [
#         [7 , 2 , 0 , 0 , 4 , 0 , 0 , 0 , 3],
#         [0 , 0 , 0 , 0 , 0 , 0 , 8 , 9 , 0],
#         [9 , 0 , 8 , 0 , 0 , 0 , 0 , 0 , 0],
#         [0 , 0 , 7 , 0 , 8 , 0 , 0 , 0 , 0],
#         [0 , 5 , 1 , 7 , 0 , 4 , 9 , 0 , 8],
#         [0 , 8 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
#         [0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 7],
#         [0 , 0 , 0 , 4 , 0 , 0 , 0 , 0 , 0],
#         [8 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
#         ]

board = config_board
pp = pprint.PrettyPrinter(width=41, compact=True)
print('--Sudoku Unsolved--')
pp.pprint(board)
solve(board)
print('--Sudoku Solved--')
pp.pprint(board)
