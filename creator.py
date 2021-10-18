import pprint
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

# produce board using randomized baseline pattern
board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
full_board = []
for line in board: 
    # print(line)
    full_board.append(line)
pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(full_board)
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
pp.pprint(config_board)