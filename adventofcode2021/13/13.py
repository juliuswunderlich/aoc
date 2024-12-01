import copy
import numpy as np
"""
TESTINPUT FOLDS
fold along y=7
fold along x=5
"""
instr = [("x",655),
("y",447),
("x",327),
("y",223),
("x",163),
("y",111),
("x",81),
("y",55),
("x",40),
("y",27),
("y",13),
("y",6)]

def foldAlongX(points, val):
    res = []
    for p in points:
        x = p[0]
        if x > val: p[0] = 2*val-x
        if p not in res: res.append(p)
    return copy.deepcopy(res)

def foldAlongY(points, val):
    res = []
    for p in points:
        y = p[1]
        if y > val: p[1] = 2*val-y
        if p not in res: res.append(p)
    return copy.deepcopy(res)

fname = "13/input.txt"
f = open(fname, 'r')
points = [[int(el) for el in l.strip().split(',')] for l in f]

# 729
res = copy.deepcopy(points)
for i in instr:
    if i[0] == "x":
        res = foldAlongX(res, i[1])
    else:
        res = foldAlongY(res, i[1])

xes = []
yes = []
# 38

arr = np.zeros((50,50))
for val in res:
    arr[val[0]][val[1]] = 5

np.savetxt('test.txt', arr, fmt="%1.0f")


