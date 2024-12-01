# string is exactly 512 characters long
import numpy as np

def checkWhereMiss(n):
    if not 0 <= n[0] <= WIDTH-1:
        if n[0] < 0: return 'l'
        elif n[0] > WIDTH-1: return 'r'
    if not 0 <= n[1] <= HEIGHT-1:
        if n[1] < 0: return 'u'
        elif n[1] > HEIGHT-1: return 'd'
    else:
        raise ValueError

def checkInGrid(n):
    global WIDTH, HEIGHT
    return 0 <= n[0] <= WIDTH-1 and 0 <= n[1] <= HEIGHT-1

def expandGrid(g):
    global WIDTH, HEIGHT
    row = np.full((1,WIDTH), '.')
    g = np.concatenate((row, g), 0)
    g = np.concatenate((row, g), 0)
    g = np.concatenate((g, row), 0)
    g = np.concatenate((g, row), 0)
    HEIGHT += 4
    col = np.full((HEIGHT,1), '.')
    g = np.concatenate((col, g), 1)
    g = np.concatenate((col, g), 1)
    g = np.concatenate((g, col), 1)
    g = np.concatenate((g, col), 1)
    WIDTH += 4
    return np.array(g, copy=True)





def decodePoint(g, g_new,p):
    global algo
    x = p[1]
    y = p[0]
    for p in [(y-1,x-1), (y-1, x), (y-1, x+1),(y,x-1), (y,x), (y, x+1), (y+1,x-1), (y+1, x), (y+1,x+1)]:
        if not checkInGrid(p): return
    lup = [g[y-1,x-1], g[y-1, x], g[y-1, x+1]]
    lmi = [g[y,x-1], g[y,x], g[y, x+1]]
    ldo = [g[y+1,x-1], g[y+1, x], g[y+1,x+1]]
    if lup + lmi + ldo == ['.'] *9:
        g_new[y][x] = '#'
        return
    num = int("".join(['0' if c == '.' else '1' for c in lup+lmi+ldo]), 2) # get the num
    g_new[y][x] = algo[num] # lookup



def onePass(g, a):
    global HEIGHT, WIDTH
    # first expand
    g = expandGrid(g)
    #print(g)
    # indented starting points after expansion
    #g_new = np.array(g, copy=True)
    g_new = np.full_like(g, '.')
    for y in range(1, HEIGHT-1):
        for x in range(1, WIDTH-1):
            decodePoint(g, g_new, (y,x))
    return np.array(g_new, copy=True)











fname = "20/input.txt"
f = open(fname, 'r')

data = [[s.split() for s in l.strip()] for l in f]
algo = np.squeeze(data[0])
assert(len(algo) == 512)
data = np.squeeze(np.array(data[2:]))
HEIGHT = len(data)
WIDTH = len(data[0])

for _ in range(2):
    data = onePass(data, algo)
counter = 0
for x in range(len(data[0])):
    for y in range(len(data)):
        if data[y][x] == '#': counter += 1
print(counter)


