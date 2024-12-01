import numpy as np
import copy

fname = "input.txt"
f = open(fname, 'r')

nmap = {}
data = [list(map(lambda x: int(x), l.strip())) for l in f]
for y in range(len(data)):
    for x in range(len(data[0])):
        nmap[(x,y)] = []
        my = len(data)-1
        mx = len(data[0])-1

        up = (y-1, x)
        down = (y+1, x)
        left = (y, x-1)
        right = (y, x+1)

        # linker rand
        if left[1] < 0:
            #obere ecke
            if up[0] < 0:
                nmap[(x,y)].append((data[down[0]][down[1]], (down[1], down[0])))
                nmap[(x,y)].append((data[right[0]][right[1]], (right[1], right[0])))
            # untere ecke
            elif down[0] > my:
                nmap[(x,y)].append((data[right[0]][right[1]], (right[1], right[0])))
                nmap[(x,y)].append((data[up[0]][up[1]], (up[1], up[0])))
            # seite
            else:
                nmap[(x,y)].append((data[right[0]][right[1]], (right[1], right[0])))
                nmap[(x,y)].append((data[up[0]][up[1]], (up[1], up[0])))
                nmap[(x,y)].append((data[down[0]][down[1]], (down[1], down[0])))
        elif right[1] > mx:
            # obere ecke
            if up[0] < 0:
                nmap[(x,y)].append((data[down[0]][down[1]], (down[1], down[0])))
                nmap[(x,y)].append((data[left[0]][left[1]], (left[1], left[0])))
            # untere ecke
            elif down[0] > my:
                nmap[(x,y)].append((data[left[0]][left[1]], (left[1], left[0])))
                nmap[(x,y)].append((data[up[0]][up[1]], (up[1], up[0])))
            # seite
            else:
                nmap[(x,y)].append((data[left[0]][left[1]], (left[1], left[0])))
                nmap[(x,y)].append((data[up[0]][up[1]], (up[1], up[0])))
                nmap[(x,y)].append((data[down[0]][down[1]], (down[1], down[0])))
        elif up[0] < 0:
            nmap[(x,y)].append((data[left[0]][left[1]], (left[1], left[0])))
            nmap[(x,y)].append((data[right[0]][right[1]], (right[1], right[0])))
            nmap[(x,y)].append((data[down[0]][down[1]], (down[1], down[0])))
        elif down[0] > my:
            nmap[(x,y)].append((data[left[0]][left[1]], (left[1], left[0])))
            nmap[(x,y)].append((data[right[0]][right[1]], (right[1], right[0])))
            nmap[(x,y)].append((data[up[0]][up[1]], (up[1], up[0])))
        else:
            nmap[(x,y)].append((data[left[0]][left[1]], (left[1], left[0])))
            nmap[(x,y)].append((data[right[0]][right[1]], (right[1], right[0])))
            nmap[(x,y)].append((data[up[0]][up[1]], (up[1], up[0])))
            nmap[(x,y)].append((data[down[0]][down[1]], (down[1], down[0])))


        
mins = []
lpoints = []

for y in range(len(data)):
    for x in range(len(data[0])):
        val = data[y][x]
        if  val < min(list(map(lambda x: x[0], nmap[(x,y)]))):
            lpoints.append((x,y))
            mins.append(val)

mins = list(map(lambda x : x+1, mins))
summ = 0
for val in mins: summ+= val
print(summ)


# 498

# modify with 9 as blockers
# add left and right
for i in range(len(data)):
    data[i].append(9)
    data[i].insert(0, 9)

# add top and bottom
data.append([9] * (len(data[0])))
data.insert(0, [9] * (len(data[0])))

def buildbasin(y, x, c):
    if data[y][x] != 9:
        c += 1 # count the number of filled-in 9s
        data[y][x] = 9 # fill
        c = buildbasin(y, x+1, c)
        c = buildbasin(y, x-1, c)
        c = buildbasin(y+1, x, c)
        c = buildbasin(y-1, x, c)
    return c

basins = []
for row in range(1, len(data)-1):
    for col in range(1, len(data[0])-1):
        b = buildbasin(row, col, 0)
        if b != 0:
            basins.append(b)

basins.sort()
res = basins[-1] * basins[-2] * basins[-3]
print(res)





#105 102 100
# 1071000