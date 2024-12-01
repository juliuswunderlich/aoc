from collections import Counter
s = [l.strip() for l in open('input.txt', 'r')]

C = Counter()




def fun():
    res = 0
    while 1:
        for el in s:
            res += int(el)
            #print(res)
            C[res] += 1
            if C[res] > 1:
                return res


print(fun())


