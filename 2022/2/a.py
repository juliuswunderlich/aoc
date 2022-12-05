in_gen = (l.strip().split(' ') for l in open('in.txt', 'r'))
# 0 loss, 3 draw, 6 win
# 1 rock, 2 paper, 3 scissor

plays = {
    'A': 1,
    'X' : 1,
    'B' : 2,
    'Y' : 2,
    'C': 3,
    'Z' : 3
}


win = 6
draw = 3
loss = 0

def play(op, me):
    op_val = plays[op]
    me_val = plays[me]
    if op_val == me_val:
        return draw + me_val
    if op == 'A':
        if me == 'Y':
            return win + me_val
        if me == 'Z':
            return loss + me_val
    elif op == 'B':
        if me == 'X':
            return loss + me_val
        if me == 'Z':
            return win + me_val
    elif op == 'C':
        if me == 'X':
            return win + me_val
        if me == 'Y':
            return loss + me_val


def beat(op, me):
    if me == 'X': # lose
        if op == 'A': #rock
            return loss + plays['Z']
        if op == 'B': # paper
            return loss + plays['X']
        if op == 'C': # scissor
            return loss + plays['Y']
    elif me == 'Y': #draw
        if op == 'A': #rock
            return draw + plays['X']
        if op == 'B': # paper
            return draw + plays['Y']
        if op == 'C': # scissor
            return draw + plays['Z']
    elif me == 'Z': #win
        if op == 'A': #rock
            return win + plays['Y']
        if op == 'B': # paper
            return win + plays['Z']
        if op == 'C': # scissor
            return win + plays['X']

score = 0
for op, me in iter(in_gen):
    #score += play(op, me)
    score += beat(op, me)

print(score)


