import re














if __name__ == "__main__":
    #input = ['F10','N3','F7','R90','F11']
    input = [l.strip() for l in open("input.txt")]
    directions = ['E', 'S', 'W', 'N']
    neg_directions = ['E', 'N', 'W', 'S']
    # directions n, e, s, w - start in e
    # n, e will be positive values 
    # s, w will be negative values
    ship = [0,0,'E'] #(x,y, direction)
    for inst in input:
        move = inst[0]
        val = int(re.split("^\w",inst)[1])
        if move == 'F':
            move = ship[2]
        if move == 'N':
            ship[1] += val
        if move == 'S':
            ship[1] -= val

        if move == 'E':
            ship[0] += val
        if move == 'W':
            ship[0] -= val

        if move == 'R':
            times = int(val/90) # how many turns
            pos = [i for i in range(4) if directions[i] == ship[2]]
            assert(len(pos) == 1)
            i = pos[0] # what i am i in directions
            i = (i + times)%4
            ship[2] = directions[i]

        if move == 'L':
            times = int(val/90) # how many turns
            pos = [i for i in range(4) if neg_directions[i] == ship[2]]
            assert(len(pos) == 1)
            i = pos[0] # what i am i in directions
            i = (i + times)%4
            ship[2] = neg_directions[i]
    print(ship[0] + abs(ship[1]))

