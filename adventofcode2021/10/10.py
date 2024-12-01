fname = "input.txt"

f = open(fname, 'r')
data = [list(map(lambda x: x, l.strip())) for l in f]

mapCloseOpen = {
    "}":"{",
    "]":"[",
    ">":"<",
    ")":"(",
}
mapOpenClose= {
    "{":"}",
    "[":"]",
    "<":">",
    "(":")",
}


map = {
    "{": 0, "}":0,
    "[": 0, "]":0,
    "(": 0, ")":0,
    "<": 0, ">":0,
}
stack = []
wrongs = []
incomplete = []
def checkLine(data):
    for line in data:
        w = False
        for i,c in enumerate(line):
            if c in mapOpenClose.keys():
                stack.append(c)
            elif c in mapCloseOpen.keys():
                old = stack.pop()
                if c != mapOpenClose[old]:
                    w = True
                    wrongs.append(c)
                    #print("expected {0} but found {1}".format( mapOpenClose[old], c))
        if not w:
            incomplete.append(line)




checkLine(data)
summ = 0
for c in wrongs:
    if c == ')':
        summ += 3
    elif c == ']':
        summ += 57
    elif c == '}':
        summ += 1197
    elif c == '>':
        summ += 25137
print(summ)

values = {")":1, "]":2, "}":3, ">":4}

# part two
def calcScore(l):
    score = 0
    for x in l:
        score *= 5
        score += values[x]
    return score





summs = []
for line in incomplete:
        stack = []
        for i,c in enumerate(line):
            if c in mapOpenClose.keys():
                stack.append(c)
            elif c in mapCloseOpen.keys():
                stack.pop()
                #stack.remove(mapCloseOpen[c])
        corrections = []
        stack.reverse()
        for c in stack:
            corrections.append(mapOpenClose[c])
        summs.append(calcScore(corrections))

summs.sort()
print(summs[int(len(summs)/2)])


    



            

        
    



checkLine(data)
        



