import numpy as np
import itertools
import copy

f = open("input.txt", 'r')
f2 = open("input_nofirst.txt", 'r')

numbers = [int(i) for i in f.readline().strip().split(',')]
boards = []
boards_t = []

# wichtig
lines = []
cols = []

board = []
i = 0
for line in f2:
    if line == "\n":
        continue
    nums = []
    for j in line.strip().split(' '):
        if j != '':
            nums.append(int(j))
    assert(len(nums) == 5)
    board.append(nums)
    lines.append(nums)
    i += 1
    if (i == 5):
        i = 0
        assert(len(board) == 5)
        boards.append(board)
        b_t = (np.array(board).T).tolist()
        boards_t.append(b_t)
        for l in b_t:
            cols.append(l)
        board = []

def getPosVal(val):
    for i in range(len(numbers)):
        if numbers[i] == val:
            return i

def getSum(zeile):
    s = 0
    for b in boards:
        for l in b:
            if zeile == l:
                b.remove(l)
        for l in b:
            for val in l:
                s += val
    return s

def howLongDoesItTake(vals):
    s = 0
    for i in range(len(numbers)):
        for v in vals:
            if numbers[i] == v:
                s+= i
    return s


def play(lines):
    lines_orig = copy.deepcopy(lines)
    cols_orig = copy.deepcopy(cols)
    for n in numbers:
        for i,j in zip(range(len(lines)), range(len(cols))):
            if n in lines[i] :
                lines[i].remove(n)
                if len(lines[i]) == 0:
                    if n not in winning_row_vals: winning_row_vals.append(n)
                    if n == 15:
                        print("lines")
                        print(lines_orig[i])
                        print(n)
                        return
            if n in cols[i]:
                cols[i].remove(n)
                if len(cols[i]) == 0:
                    if n not in winning_col_vals: winning_col_vals.append(n)
                    if n == 15:
                        print("cols")
                        print(cols_orig[i])
                        print(n)
                        return
                    
np_boards = []

for b in boards:
    np_boards.append(np.array(b).astype(str))

winning_boards = []
winning_vals = []

def playBoardwise():
    for i,n in enumerate(numbers):
        for j,b in enumerate(np_boards):
            old = b
            b = np.where(b == str(n), 'x', b)
            np_boards[j] = b
        for j,b in enumerate(np_boards):
            if ['x', 'x', 'x', 'x', 'x'] in (b.tolist()):
                winning_boards.append(b)
                if n not in winning_vals: winning_vals.append(n)
                del np_boards[j]
                continue
            if ['x', 'x', 'x', 'x', 'x'] in (b.T.tolist()):
                winning_boards.append(b)
                if n not in winning_vals: winning_vals.append(n)
                del np_boards[j]


playBoardwise()

print("Math")
sum = 0
for val in winning_boards[-1].flatten().tolist():
    if val != 'x':
        sum += int(val)
print("sum: ", sum)
print("res: ", sum*winning_vals[-1])