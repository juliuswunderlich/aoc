import numpy as np

f = open('input.txt', 'r')
lines = [l.strip() for l in f]
numbers = []
for i in range(len(lines)):
    numbers.append([int(c) for c in lines[i]])

N = np.array(numbers).reshape(1000, 12)
C = np.sum(N, 0) # get column sums
print(C)
G = (C > 500).astype(int)
E = (G == 0).astype(int)
gamma = "".join([str(i) for i in G.tolist()])
epsilon = "".join([str(i) for i in E.tolist()])
#print(gamma, epsilon)
# use external converter because it is a pain in python
gamma = 1508
epsilon = 2587
#print(gamma * epsilon)

# part two
def getMaxAtPosOxygen(numbers, pos):
    c_0 = 0
    c_1 = 0
    for num in numbers:
        if num[pos] == 0: c_0 += 1
        elif num[pos] == 1: c_1+= 1
    if c_0 > c_1: return 0
    elif c_1 > c_0: return 1
    else: return 1

def getMaxAtPosScrubber(numbers, pos):
    c_0 = 0
    c_1 = 0
    for num in numbers:
        if num[pos] == 0: c_0 += 1
        elif num[pos] == 1: c_1+= 1
    if c_0 < c_1: return 0
    elif c_1 < c_0: return 1
    else: return 0





numbers = N.tolist()
for pos in range(12):
    req_val = getMaxAtPosOxygen(numbers, pos)
    #print(req_val)
    numbers = [num for num in numbers if num[pos] == req_val ]
    print(len(numbers))
    if len(numbers) == 1:
        break

numbers = N.tolist()
for pos in range(12):
    req_val = getMaxAtPosScrubber(numbers, pos)
    #print(req_val)
    numbers = [num for num in numbers if num[pos] == req_val ]
    print(len(numbers))
    if len(numbers) == 1:
        break

print("".join([str(i) for i in numbers]))
oxygen = 1639
scrubber = 2692
print(oxygen * scrubber)









