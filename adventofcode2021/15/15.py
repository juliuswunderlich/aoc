import copy, sys, numpy as np

fname = "15/input.txt"
f = open(fname, 'r')
map = [[int(c) for c in l.strip()] for l in f]
HEIGHT = 0
WIDTH = 0

# build adjacency matrix
adj = {}


for y in range(len(map)):
    for x in range(len(map[0])):
        neighbors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        adj[(x,y)] = []
        for n in neighbors:
            if 0 <= n[0] <= WIDTH-1 and 0 <= n[1] <= HEIGHT-1:
                adj[(x,y)].append(n)


class Cell:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist

def checkInGrid(n):
    return 0 <= n[0] <= WIDTH-1 and 0 <= n[1] <= HEIGHT-1

def shortest(map, row, col):
    # initialize distances with max int
    dis = copy.deepcopy(map)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            dis[i][j] = sys.maxsize
    
    # stack
    st= []
    st.append(Cell(0,0,0)) # append the start cell

    # set dist to map value
    dis[0][0] = map[0][0]

    # start dijkstra
    while(len(st) != 0):
        k = st.pop()
        # check all neighbors
        x = k.x
        y = k.y
        for n in [(x-1,y),(x,y+1),(x+1,y),(x,y-1)]:
            if not checkInGrid(n):
                continue # skip if not in grid
            # wenn die distanz von der aktuellen zelle kleiner ist: update
            x = n[0]
            y = n[1]
            if (dis[x][y] > dis[k.x][k.y] + map[x][y]):
                dis[x][y] = dis[k.x][k.y] + map[x][y]
                st.append(Cell(x,y, dis[x][y]))

        st.sort(key =lambda c: (c.x, c.y), reverse=True)
    return dis[HEIGHT-1][WIDTH-1] - dis[0][0]
    #return dis[HEIGHT-1][WIDTH-1]

#print(shortest(map, HEIGHT, WIDTH))

# scale map
incr = np.vectorize(lambda x: (x+1 if x < 9 else 1))
NUM = 4
block = np.array(map)
m = np.array(map)
for i in range(NUM):
    block = incr(block)
    m = np.append(m, block, 1)
block = m
for j in range(NUM):
    block = incr(block)
    m = np.append(m, block, 0)


WIDTH = len(m[0])
HEIGHT = len(m)
print(shortest(m, HEIGHT, WIDTH))










    


