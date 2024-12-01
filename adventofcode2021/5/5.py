import numpy as np

f = open("input.txt", "r")
lines = [(x.split(','), y.split(',')) for x,y in [l.strip().split(" -> ") for l in f]]

# now to int
coord = []
for pair in lines:
    x = [int(i) for i in pair[0]]
    y = [int(i) for i in pair[1]]
    coord.append((x,y))


# find all vertical or horizontal ones
coord_horiz = []
coord_vert = []
coord_diag = []
for pair in coord:
    assert(pair[0] != pair[1]) 
    if pair[0][0] == pair[1][0]: # x is equal
        if pair[0][1] < pair[1][1]:
            coord_vert.append(pair)
        else:
            coord_vert.append( (pair[1], pair[0]) )
    elif pair[0][1] == pair[1][1]: # y is equal
        if pair[0][0] < pair[1][0]:
            coord_horiz.append(pair)
        else:
            coord_horiz.append( (pair[1], pair[0]) )

for pair in coord:
    if pair[0][0] == pair[0][1] and pair[1][0] == pair[1][1]:
        print(pair)

for pair in coord:
    if abs(pair[0][0] - pair[1][0]) == abs(pair[0][1] - pair[1][1]):
        if pair[0][0] <= pair[1][0]:
            coord_diag.append(pair)
        else:
            coord_diag.append( (pair[1], pair[0]) )



# build a map of all points
M = np.zeros((1000,1000)).tolist()

#503,56 -> 804,56
# mark all horizontal lines
for pair in coord_horiz:
    assert(pair[0][1] == pair[1][1])
    y = pair[1][1]
    for x in range(pair[0][0], pair[1][0] + 1):
        M[y][x] += 1

# mark all vert lines
for pair in coord_vert:
    assert(pair[0][0] == pair[1][0])
    x = pair[1][0]
    for y in range(pair[0][1], pair[1][1] + 1):
        M[y][x] += 1

# mark diag
for pair in coord_diag:
    assert(pair[0][0] < pair[1][0])
    if pair[0][0] == pair[0][1] and pair[1][0] == pair[1][1]:
        for i in range(pair[0][1], pair[1][1] + 1):
            M[i][i] += 1
        continue
    if (pair[0][1] < pair[1][1]):
        # ([604, 170], [928, 494])
        for i in range(0, abs((pair[1][0] - pair[0][0])) + 1):
            x = pair[0][0] + i
            y = pair[0][1] + i
            M[y][x] += 1
    else:
        #[112, 710], [368, 454])
        for i in range(0, abs((pair[1][0] - pair[0][0])) + 1):
            x = pair[0][0] + i
            y = pair[0][1] - i
            M[y][x] += 1



count = 0
for y in range(len(M)):
    for x in range(len(M[0])):
        if M[y][x] >= 2:
            count += 1

print(count)




#1254 zu low
#5197 richtig

#17552 zu low
