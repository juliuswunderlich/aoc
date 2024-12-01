num_lines = 323
num_moves_in_line = 31

def move_sled(right_step, down_step, data):
    j = 0 # start with index zero for sidesteps (right)
    i = 0 # start with index zero for linesteps (down)
    counter_tree_hits = 0
    while i < num_lines - 1:
        j = (j+right_step)%(num_moves_in_line)
        i += down_step
        if data[i][j] == '#':
            counter_tree_hits += 1
    return counter_tree_hits


# moves down: 323
# moves sideways in one line: 31
with open("input.txt") as f:
    data = [l.strip('\n') for l in f]
    num_lines = len(data)
    num_moves_in_line = len(data[0])
    x1 = move_sled(1,1, data)
    x1 *= move_sled(3,1, data)
    x1 *= move_sled(5,1, data)
    x1 *= move_sled(7,1, data)
    x1 *= move_sled(1,2, data)
    print(x1)
    # move three sidesteps right
    # if eol is reached step to beginning of line with remaining sidesteps
    # step one down




