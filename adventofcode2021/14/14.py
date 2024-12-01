import copy
import more_itertools
from more_itertools.recipes import pairwise
#templ = "NNCB"
templ = "PBVHVOCOCFFNBCNCCBHK"

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

fname = "14/input.txt"
f = open(fname, 'r')

data = [l.strip().split(" -> ") for l in f]
dd = dict(data)



def modify(word):
    word = list(word)
    i = 0
    while i < len(word)-1:
        k = word[i]+word[i+1]
        if k in dd.keys():
            word.insert(i+1, dd[k])
            i += 1
        i+=1
    return word


"""

counter = {}
for i in range(10):
    templ = modify(templ)
    for e in set(templ):
        counter[e] = templ.count(e)
        if e == 'C':
            print(counter[e])


print(counter[f])
mi = min(counter.values())
ma = max(counter.values())
print(ma - mi)
"""

# part two
instr_counter = {}
letter_counter = {}
for k in dd.keys(): instr_counter[k] = 0
for p in pairwise(templ): instr_counter[p[0]+p[1]] = 1
for l in letters: letter_counter[l] = 0
for l in templ: letter_counter[l] += 1

#NC -> B creates NB and BC
#NN -> C creates NC and CN
#CB -> H creates CH and HB

def count():
    global instr_counter
    do = []
    subinstr_counter = dict.fromkeys(instr_counter)
    for k in subinstr_counter: subinstr_counter[k] = 0
    for k, v in zip(instr_counter.keys(), instr_counter.values()):
        if v > 0:
            do.append(k)
    for i in do:
        subin1 = i[0] + dd[i]
        subin2 = dd[i] + i[1]
        val = instr_counter[i]
        letter_counter[dd[i]] += val
        subinstr_counter[subin1] += val
        subinstr_counter[subin2] += val
    instr_counter = subinstr_counter


for i in range(10):
    count()
print(letter_counter)





print(3922 -532)

