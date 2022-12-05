stacks = [
    ['W','D', 'G', 'B', 'H', 'R', 'V'],
    ['J', 'N', 'G', 'C', 'R', 'F'],
    ['L', 'S', 'F', 'H', 'D', 'N', 'J'],
     ['J', 'D', 'S', 'V'],
     ['S', 'H', 'D', 'R', 'Q', 'W', 'N', 'V'],
    ['P', 'G', 'H', 'C', 'M'],
     ['F', 'J', 'B', 'G', 'L', 'Z', 'H', 'C'],
     ['S', 'J', 'R'],
     ['L', 'G', 'S', 'R', 'B', 'N', 'V', 'M']
]



ins = []
in_gen = (i.strip().split() for i in open('in.txt', 'r'))

for el in iter(in_gen):
    nums = [int(s) for s in el if s.isdigit()]
    ins.append(nums)


def move(m, f, t):
    for i in range(m):
        stacks[t-1].append(stacks[f-1].pop())

def move2(m,f,t):
    froms = []
    for i in range(m):
        froms.append(stacks[f-1].pop())
    for i in range(m):
        stacks[t-1].append(froms.pop())


#for i in ins: move(i[0], i[1], i[2])
for i in ins: move2(i[0], i[1], i[2])


#print(stacks)
for s in stacks:
    print(s[-1], end='')
