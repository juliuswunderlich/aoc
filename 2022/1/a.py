in_gen = (l.strip() for l in open('input.txt', 'r'))

cals = []
val = 0
for el in iter(in_gen):
    if el != '': val += int(el)
    else: cals.append(val); val = 0

print("Part one: ", max(*cals))
cals.sort()
print("Part two:", sum(cals[-3:]))
