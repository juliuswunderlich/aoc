import numpy as np

fname = "11/input.txt"
f = open(fname, 'r')

grid = [list(map(lambda x: int(x), l.strip())) for l in f]
flashes = 0

def checkAllLit(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] != 0:
                return False
    return True

def glowStep(matrix):
    # increase
    matrix = (np.array(matrix) + 1).tolist()
    width = len(matrix)
    height = len(matrix[0])
    def fill(x,y):
        if matrix[x][y] == 0:
            return
        #if the square is not the new color
        elif matrix[x][y] <= 9:
            return
        elif matrix[x][y] > 9:
            matrix[x][y] = 0
            global flashes
            flashes += 1
            neighbors = [(x-1,y),(x+1,y),(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x,y-1),(x,y+1)]
            for n in neighbors:
                if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
                    # increase neighbors
                    if (matrix[n[0]][n[1]]) != 0:
                        matrix[n[0]][n[1]] += 1
                    fill(n[0],n[1])
    # find all startvals
    for x in range(width):
        for y in range(height):
            if matrix[x][y] > 9:
                start_x = x
                start_y = y
                fill(start_x,start_y)
    return matrix

for i in range(2000):
    grid= glowStep(grid)
    if (checkAllLit(grid)):
        print(i+1)
print(np.array(grid))
print(flashes)

