"""
# part one
correct = {
    1: 2,
    4: 4,
    7: 3,
    8: 7,
}

f = open("input.txt", 'r')

signals = []
outputs = []

for l in f:
    s = ["".join(sorted(str(s).strip())) for s in l.split('|')[0].split(' ')]
    o = ["".join(sorted(str(s).strip())) for s in l.split('|')[1].split(' ')]
    s = list(filter(lambda a: a != '' and len(a) in (correct.values()), s))
    o = list(filter(lambda a: a != '' and len(a) in correct.values(), o))
    signals.append(s)
    outputs.append(o)
assert(len(signals) == len(outputs))

summ = 0 #answer part one
for l in outputs: summ += len(l)
"""

# part two
partsCorresNumMap = {
    2: (1),
    3: (7),
    4: (4),
    5: (2,3,5),
    6: (0,6,9),
    7: (8)
}

correctMapping = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
"""
acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1
"""

def whichNum(words, found):
    for s in words:
        l = len(s)
        if l == 2: found[1] = s
        elif l == 3: found[7] = s
        elif l == 4: found[4] = s
        else: found[8] = s
    for s in words:
        if len(s) == 6 and len(s - found[4]) == 2: found[9] = s
        if len(s) == 5 and len(s - found[1]) == 3: found[3] = s
    for s in words:
        if len(s) == 6 and s != found[9] and len(s - found[1]) == 4: found[0] = s
    for s in words:
        if len(s) == 6 and s != found[0] and s != found[9]: found[6] = s
    for s in words:
        if len(s) == 5 and s != found[3] and len(s - found[6]) == 0: found[5] = s
    for s in words:
        if len(s) == 5 and s != found[3] and s != found[5]: found[2] = s
    return found



f = open("testInput.txt", 'r')

signals = []
outputs = []
easy_nums = [1,4,7,8]

for l in f:
    s = ["".join(sorted(str(s).strip())) for s in l.split('|')[0].split(' ')]
    o = ["".join(sorted(str(s).strip())) for s in l.split('|')[1].split(' ')]
    signals.append(s)
    outputs.append(o)
assert(len(signals) == len(outputs))

for i,l in enumerate(signals, outputs):
    nums = []


# check which easy nums we have
"""
# check 5 nums
- 
    - 
    - 
"""