f = open("input.txt", 'r')
instructions = [l.strip().split(' ') for l in f]
depth = 0
horiz = 0
aim = 0
"""
PART 1
for ins, val in instructions:
    if ins == 'forward':
        horiz += int(val)
    elif ins == 'down':
        depth += int(val)
    elif ins == 'up':
        depth -= int(val)
print(depth * horiz)
"""

for ins, val in instructions:
    if ins == 'forward':
        horiz += int(val)
        depth += (aim * int(val))
    elif ins == 'down':
        aim += int(val)
    elif ins == 'up':
        aim -= int(val)
print(depth * horiz)