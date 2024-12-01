import numpy as np
import csv
import re

#start by saving the input as a matrix
#TODO: scrape the input from the website

FILENAME = 'input.csv'

CABLE_ONE = []
CABLE_TWO = []
GRID_SIZE = 0
CROSSES = []

STARTING_POINT = [0,0]

def read_input():
    with open(FILENAME) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_count = 0
        for row in csv_reader:
            if row_count == 0:
                CABLE_ONE = row
                row_count += 1
                pass
            elif row_count == 1:
                CABLE_TWO = row

    return CABLE_ONE, CABLE_TWO

def get_grid_size(cable_one, cable_two):
    sizes_one = []
    sizes_two = []
    pattern = '[0-9]+'
    for val in cable_one:
        sizes_one.append(re.findall(pattern, val))
    for val in cable_two:
        sizes_two.append(re.findall(pattern, val))

    sizes_one = [int(item) for sublist in sizes_one for item in sublist]
    sizes_two = [int(item) for sublist in sizes_two for item in sublist]

    return max( sum(sizes_one), sum(sizes_two))

def get_shortest_cross(grid_size):
    grid = np.zeros((grid_size, grid_size), int)
    print("before: \n", grid)

    grid = draw_path(CABLE_ONE, grid)

    print("after: \n", grid)
    grid = draw_path(CABLE_TWO, grid)
    print("after: \n", grid)

    #iterate and find shortest -1 in the grid
    dist, min = 0, 0
    min_coord = [0,0]

    for i in CROSSES:
        dist = calc_man_dist(i)
        if min == 0:
            min = dist
            min_coord = i
        else:
            if min <= dist:
                pass
            else:
                min = dist
                min_coord = i

    return min_coord


def calc_man_dist(coord):
    d1, d2 = 0, 0
    d1 = abs(STARTING_POINT[0] - coord[0])
    d2 = abs(STARTING_POINT[1] - coord[1])

    return d1 + d2

    
def draw_path(cable, grid):
    directions = []
    step_size = []

    pattern_directions = '[A-Z]{1}'
    pattern_step_size = '[0-9]+'
    
    for val in cable:
        directions.append(re.findall(pattern_directions, val))
    for val in cable:
        step_size.append(re.findall(pattern_step_size, val))

    directions = [item for sublist in directions for item in sublist]
    step_size = [int(item) for sublist in step_size for item in sublist]

    print("Directions: ", directions)
    print("Step-sizes: ", step_size)

    assert(len(directions) == len(step_size))

    #start in the middle of the grid
    #NOTE: Stuff is flipped by 90 degrees clockwise
    s = STARTING_POINT
    print("startpunkt: ", s)
    step = 0;
    for j in range(len(directions)):
        step = step_size[j]
        if directions[j] == 'U':
            for i in range(step + 1):
                x = s[0] + 0
                y = s[1] + i
                if grid[x][y] == 1 and i != 0:
                    grid[x][y] = -1
                    CROSSES.append([x,y])
                else:
                    grid[x][y] = 1
            s = [x,y]

        if directions[j] == 'D':
            for i in range(step + 1):
                x = s[0] + 0
                y = s[1] - i
                if grid[x][y] == 1 and i != 0:
                    grid[x][y] = -1
                    CROSSES.append([x,y])
                else:
                    grid[x][y] = 1
            s = [x,y]

        if directions[j] == 'L':
            for i in range(step + 1):
                x = s[0] - i
                y = s[1] + 0
                if grid[x][y] == 1 and i != 0:
                    grid[x][y] = -1
                    CROSSES.append([x,y])
                else:
                    grid[x][y] = 1
            s = [x,y]

        if directions[j] == 'R':
            for i in range(step + 1):
                x = s[0] + i
                y = s[1] + 0
                if grid[x][y] == 1 and i != 0:
                    grid[x][y] = -1
                    CROSSES.append([x,y])
                else:
                    grid[x][y] = 1
            s = [x,y]
    
    return grid


if __name__ == "__main__":
    min_cross = [0,0]
    CABLE_ONE, CABLE_TWO = read_input()
    GRID_SIZE = get_grid_size(CABLE_ONE, CABLE_TWO)*2
    STARTING_POINT = [int(GRID_SIZE/2),int(GRID_SIZE/2)]
    min_cross  = get_shortest_cross(GRID_SIZE)

    print("Die kürzeste Kreuzung: ", min_cross)
    print("Mit einer Distanz von: ", calc_man_dist(min_cross))
    

