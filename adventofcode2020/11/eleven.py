#!/usr/bin/python3

def readInput():
    with open('input.txt', 'r') as file:
        data = file.read()
    lines = list()
    for d in data.split("\n"):
        if (d != ""):
            lines.append(list(d))
    return lines

def compare(array2d1,array2d2):
    for i in range(len(array2d1)):
        for j in range(len(array2d1[i])):
            if (array2d1[i][j] != array2d2[i][j]):
                return False
    return True

def getValue(array2d, i, j):
    if (i < 0 or j < 0 or i >= len(array2d) or j >= len(array2d[0])):
        return ''
    else:
        return array2d[i][j]       

def deepCopy(array2d1):
    array2d2 = list()
    for i in range(len(array2d1)):
        array2d2.append(list())
        for j in range(len(array2d1[i])):
            array2d2[i].append(array2d1[i][j])
    return array2d2

def printArray(cycles, array2d):
    print('Round', cycles)
    for i in array2d:
        for j in i:
            print(j,end='')
        print()
    print()

def countSeats(lines):
    seats = 0
    for l in lines:
        seats += l.count('#')
    return seats

def occupiedSeatsVisible(array2d, i, j):
    around = ['?','?','?',
              '?',    '?',
              '?','?','?']
    radius = 1
    while around.count('?') > 0:
        if (around[0] == '?'): # top left
            t = getValue(array2d, i-radius, j-radius)
            if t in ['#','L','']: around[0] = t
        if (around[1] == '?'): # top
            t = getValue(array2d, i-radius, j)
            if t in ['#','L','']: around[1] = t
        if (around[2] == '?'): # top right
            t = getValue(array2d, i-radius, j+radius)
            if t in ['#','L','']: around[2] = t
        if (around[3] == '?'): # left
            t = getValue(array2d, i,        j-radius)
            if t in ['#','L','']: around[3] = t
        if (around[4] == '?'): # right
            t = getValue(array2d, i,        j+radius)
            if t in ['#','L','']: around[4] = t
        if (around[5] == '?'): # bottom left
            t = getValue(array2d, i+radius, j-radius)
            if t in ['#','L','']: around[5] = t
        if (around[6] == '?'): # bottom
            t = getValue(array2d, i+radius, j)
            if t in ['#','L','']: around[6] = t
        if (around[7] == '?'): # bottom right
            t = getValue(array2d, i+radius, j+radius)
            if t in ['#','L','']: around[7] = t
        # increase search radius
        radius += 1
    return around

def part1():
    lines = readInput()
    modified = True
    cycles = 0
    while modified:
        cycles += 1
        linesNext = deepCopy(lines)
        for i in range(len(linesNext)):
            for j in range(len(linesNext[0])):
                if (lines[i][j] in ['L','#']):
                    t = [getValue(lines,i-1,j-1), getValue(lines,i-1,j), getValue(lines,i-1,j+1),
                        getValue(lines,i  ,j-1),                         getValue(lines,i  ,j+1),
                        getValue(lines,i+1,j-1), getValue(lines,i+1,j), getValue(lines,i+1,j+1)]
                    if (t.count('#') == 0):
                        linesNext[i][j] = '#'
                    elif (t.count('#') >= 4):
                        linesNext[i][j] = 'L'
        #printArray(cycles, lines)
        modified = not compare(lines, linesNext)
        lines = deepCopy(linesNext)
    print('after',cycles,'rounds',countSeats(lines),'seats are in use')

def part2():
    lines = readInput()
    modified = True
    cycles = 0
    while modified:
        cycles += 1
        linesNext = deepCopy(lines)
        for i in range(len(linesNext)):
            for j in range(len(linesNext[0])):
                if (lines[i][j] in ['L','#']):
                    t = occupiedSeatsVisible(lines,i,j)
                    if (t.count('#') == 0):
                        linesNext[i][j] = '#'
                    elif (t.count('#') >= 5 and lines[i][j] in ['L','#']):
                        linesNext[i][j] = 'L'
        #printArray(cycles, lines)
        modified = not compare(lines, linesNext)
        lines = deepCopy(linesNext)
    print('after',cycles,'rounds',countSeats(lines),'seats are in use')

part1()
part2()









"""
nrows = 0
ncols = 0
input = []

# returns true if there are only free seats next to it
def checkHorizontal(i,j):
    b = True
    c = 0
    if j == 0:
        if input[i][j+1] == "#":
            c += 1
            b = False
    elif j == ncols-1:
        if input[i][j-1] == '#':
            c += 1
            b = False
    else:
        if input[i][j+1] == "#":
            c += 1
            b = False
        if input[i][j-1] == '#':
            c += 1
            b = False
    return b,c

def checkVertical(i, j):
    b = True
    c = 0
    if i == 0:
        if input[i+1][j] == "#":
            c += 1
            b = False
    elif i == nrows-1:
        if input[i-1][j] == '#':
            c += 1
            b = False
    else:
        if input[i+1][j] == "#":
            c += 1
            b = False
        if input[i-1][j] == '#':
            c += 1
            b = False
    return b,c

def checkDiagonal(i,j):
    b = True
    c = 0
    if i == 0: # in first row
        if j == 0:
            if input[i+1][j+1] == '#':
                b = False
                c += 1
            if j == ncols-1:
                if input[i+1][j-1] == '#':
                    b = False
                    c += 1
    elif i == nrows - 1: # in last row
        if j == 0:
            if input[i-1][j+1] == '#':
                b = False
                c += 1
            if j == ncols-1:
                if input[i-1][j-1] == '#':
                    b = False
                    c += 1
    elif j == ncols-1:
        if input[i+1][ j-1]:
            b = False
            c += 1
        if input[i-1][ j-1]:
            b = False
            c += 1
    elif j == 0:
        if input[i+1][ j+1]:
            b = False
            c += 1
        if input[i-1][ j+1]:
            b = False
            c += 1
    else:
        assert(i != 0 and j != 0)
        assert(i != nrows-1 and j != ncols-1)
        if input[i-1][j+1] == '#':
            b = False
            c += 1
        if input[i-1][j+1] == '#':
            b = False
            c += 1
        if input[i+1][j-1] == '#':
            b = False
            c += 1
        if input[i+1][j+1] == '#':
            b = False
            c += 1

    return b,c


def checkAdjazent(i, j):
    adjacend = True
    h,ch = checkHorizontal(i,j)
    v,vh = checkVertical(i,j)
    d,dh = checkDiagonal(i,j)
    if not h:
        adjacend = False # occupied seat in adjacency
    if not v:
        adjacend = False # occupied seat in adjacency
    if not d:
        adjacend = False # occupied seat in adjacency
    return adjacend, ch+vh+dh


if __name__ == "__main__":
    input = [list(l.strip()) for l in open("test_input.txt")]
    [print(l) for l in input]
    print()
    ncols = len(input[0])
    nrows = len(input)

    for i in range(len(input)):
        for j in range(len(input[0])):
            b,c = checkAdjazent(i,j)
            print(c)
            if b and input[i][j] == 'L':
                input[i][j] = '#'
                continue
            if input[i][j] == '#' and c >= 4:
                input[i][j] = 'L'
    [print(l) for l in input]
"""
